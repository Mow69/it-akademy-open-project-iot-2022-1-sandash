<?php

namespace App\Repository;

use App\Entity\Task;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @method Task|null find($id, $lockMode = null, $lockVersion = null)
 * @method Task|null findOneBy(array $criteria, array $orderBy = null)
 * @method Task[]    findAll()
 * @method Task[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class TaskRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Task::class);
    }

        /**
     * Find three next task
     * @return Task[] Returns an array of Task objects
     */
    public function findThreeNewTask(): ?Array
    {
        $now = new \DateTime('now');

        $request = $this->createQueryBuilder('t')
            ->Where('t.start >= :todayStart AND t.start <= :todayEnd')
            ->andWhere('t.end > :now')
            ->setMaxResults(3)
            ->setParameter('now', $now)
            ->setParameter('todayStart', $now->format('Y-m-d 00:00:00'))
            ->setParameter('todayEnd',   $now->format('Y-m-d 23:59:59'))
            ->orderBy('t.start', 'ASC')
            ;

        $query = $request->getQuery();

        return $query->execute();
    }

    // /**
    //  * @return Task[] Returns an array of Task objects
    //  */
    /*
    public function findByExampleField($value)
    {
        return $this->createQueryBuilder('t')
            ->andWhere('t.exampleField = :val')
            ->setParameter('val', $value)
            ->orderBy('t.id', 'ASC')
            ->setMaxResults(10)
            ->getQuery()
            ->getResult()
        ;
    }
    */

    /*
    public function findOneBySomeField($value): ?Task
    {
        return $this->createQueryBuilder('t')
            ->andWhere('t.exampleField = :val')
            ->setParameter('val', $value)
            ->getQuery()
            ->getOneOrNullResult()
        ;
    }
    */
}
