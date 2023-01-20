<?php

namespace App\Controller;

use App\Entity\User;
use App\Form\UserType;
use App\Repository\UserRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\EventListener\UserListener;
use Symfony\Component\HttpFoundation\JsonResponse;

#[Route('/user')]
class UserController extends AbstractController
{
    const CREATE = '/rfid/create';
    const UPDATE = '/rfid/update';
    const DELETE = '/rfid/delete';

    #[Route('/', name: 'user_index', methods: ['GET'])]
    public function index(UserRepository $userRepository): Response
    {
        return $this->render('user/index.html.twig', [
            'users' => $userRepository->findAll(),
        ]);
    }

    #[Route('/new', name: 'user_new', methods: ['GET', 'POST'])]
    public function new(Request $request,
                        EntityManagerInterface $entityManager,
                        UserListener $userListener
    ): Response
    {
        $user = new User();
        $form = $this->createForm(UserType::class, $user);
        $form->handleRequest($request);

        $user->setCreatedAt(new \DateTimeImmutable('now'));

        if ($form->isSubmitted() && $form->isValid()) {
            $entityManager->persist($user);
            $entityManager->flush();
            if($user->getRfidTag() !== null) {
                $userListener->mqttPublish($user->getId(), $user->getRfidTag(), self::CREATE);
                $this->addFlash('notice', 'This mqtt as been send: '.self::CREATE.$user->getRfidTag());
            }
            return $this->redirectToRoute('user_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('user/new.html.twig', [
            'user' => $user,
            'form' => $form,
        ]);
    }


    #[Route('/present-count', name: 'user_count', methods: ['GET'])]
    public function countPresentUsers(UserRepository $userRepository): JsonResponse
    {
        $userCount = $userRepository->findPresentUserCount();
        
        return new JsonResponse($userCount);
    }

    #[Route('/{id}', name: 'user_show', methods: ['GET'])]
    public function show(User $user): Response
    {
        return $this->render('user/show.html.twig', [
            'user' => $user,
        ]);
    }

    #[Route('/{id}/edit', name: 'user_edit', methods: ['GET', 'POST'])]
    public function edit(Request $request,
                         User $user,
                         EntityManagerInterface $entityManager,
                         UserListener $userListener
    ): Response
    {
        $form = $this->createForm(UserType::class, $user);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $entityManager->flush();
            if($user->getRfidTag() !== null){
                $userListener->mqttPublish($user->getId(), $user->getRfidTag(), self::UPDATE);
                $this->addFlash('notice', 'This mqtt as been send: '.self::UPDATE.$user->getRfidTag());

            }

            return $this->redirectToRoute('user_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('user/edit.html.twig', [
            'user' => $user,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'user_delete', methods: ['POST'])]
    public function delete(Request $request,
                           User $user,
                           EntityManagerInterface $entityManager,
                           UserListener $userListener
    ): Response
    {
        if ($this->isCsrfTokenValid('delete'.$user->getId(), $request->request->get('_token'))) {
            if($user->getRfidTag() !== null) {
                $userListener->mqttPublish($user->getId(), $user->getRfidTag(), self::DELETE);
                $this->addFlash('notice', 'This mqtt as been send: '.self::DELETE.$user->getRfidTag());
            }
            $entityManager->remove($user);
            $entityManager->flush();
        }

        return $this->redirectToRoute('user_index', [], Response::HTTP_SEE_OTHER);
    }
}
