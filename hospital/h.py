from .doctors.surgeons import get_surgeons
from .doctors.nurses import get_nurses


def get_main():
    print('Med')
    get_nurses()
    get_surgeons()