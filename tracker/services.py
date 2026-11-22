from tracker.models import AssociatedHabit, Habit


def get_habit_list(user):
    return Habit.objects.filter(owner=user)


def get_associated_habit_list(user):
    return AssociatedHabit.objects.filter(owner=user)
