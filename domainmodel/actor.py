
class Actor:

    def __init__(self, actor_full_name: str):
        self.__colleague_list = []
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        test1 = self.__actor_full_name
        test2 = other.__actor_full_name
        return test1 == test2

    def __lt__(self, other):
        test1 = self.__actor_full_name
        test2 = other.__actor_full_name
        return test1 < test2

    def __hash__(self):
        return 0

    def add_actor_colleague(self, colleague):
        if colleague not in self.__colleague_list:
            self.__colleague_list.append(colleague)
    
    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleague_list:
            return True
        else:
            return False



