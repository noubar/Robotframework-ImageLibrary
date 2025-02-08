
class CommonInput:

    @staticmethod
    def validate_int(x, exception:type[Exception]):
        """
        """
        try:
            x = int(x)
        except ValueError as e:
            raise exception(x) from e
        return x

    @staticmethod
    def validate_float(x, exception:type[Exception]):
        """
        """
        try:
            x = float(x)
        except ValueError as e:
            raise exception(x) from e
        return x

    @staticmethod
    def validate_bool(x, exception:type[Exception]):
        """
        """
        try:
            x = bool(x)
        except ValueError as e:
            raise exception(x) from e
        return x
