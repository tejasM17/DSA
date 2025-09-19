from heapq import heappush, heappop


class TaskManager:
    def __init__(self, tasks):
        print(f"Initializing with tasks: {tasks}")
        # Map taskId to [userId, priority, is_active]
        self.task_info = {}
        # Max heap for (-priority, userId, taskId)
        self.priority_heap = []

        # Process initial tasks
        for userId, taskId, priority in tasks:
            self.task_info[taskId] = [userId, priority, True]
            heappush(self.priority_heap, (-priority, userId, taskId))
            print(f"  Added taskId={taskId}, userId={userId}, priority={priority}")

    def add(self, userId: int, taskId: int, priority: int) -> None:
        print(f"Adding task: taskId={taskId}, userId={userId}, priority={priority}")
        self.task_info[taskId] = [userId, priority, True]
        heappush(self.priority_heap, (-priority, userId, taskId))
        print(f"  Heap: {self.priority_heap}")

    def edit(self, taskId: int, newPriority: int) -> None:
        print(f"Editing task: taskId={taskId}, newPriority={newPriority}")
        if taskId in self.task_info:
            self.task_info[taskId][1] = newPriority
            heappush(
                self.priority_heap, (-newPriority, self.task_info[taskId][0], taskId)
            )
            print(f"  Updated task_info: {self.task_info[taskId]}")

    def rmv(self, taskId: int) -> None:
        print(f"Removing task: taskId={taskId}")
        if taskId in self.task_info:
            self.task_info[taskId][2] = False
            print(f"  Marked taskId={taskId} inactive")

    def execTop(self) -> int:
        print("Getting highest priority task")
        while self.priority_heap:
            priority, userId, taskId = heappop(self.priority_heap)
            priority = -priority
            if (
                taskId in self.task_info
                and self.task_info[taskId][2]
                and self.task_info[taskId][1] == priority
            ):
                heappush(self.priority_heap, (-priority, userId, taskId))
                print(
                    f"  Found valid task: taskId={taskId}, userId={userId}, priority={priority}"
                )
                return userId
            print(
                f"  Skipped outdated/inactive: taskId={taskId}, userId={userId}, priority={priority}"
            )

        print("  No valid tasks")
        return -1


mytask = TaskManager(
    [
        [1, 101, 10],
        [2, 102, 20],
        [3, 103, 15],
    ]
)

mytask.add(4, 104, 5)  # Add new task
mytask.edit(101, 25)  # Edit task 101’s priority
mytask.rmv(102)  # Remove task 102
top_user = mytask.execTop()  # Execute top priority
print(f"Top priority user is: {top_user}")
