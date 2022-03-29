class Critical(Exception):
    """
    Handled in Critical Handler, will result of an critical error page display and could be result of an system exit.
    Display an critical error flash message
    """

    def __init__(self, message):
        self.message = message


class Base(Exception):
    """
    Handled in Base Handler, will result of an error page display.
    Display an base error flash message
    """

    def __init__(self, message):
        self.message = message


# --


class ServerInternalError(Critical):
    pass


class AuthentificationException(Base):
    pass


class DatabaseException(Base):
    pass


# --


class AppException(ServerInternalError):
    pass


class InitialisationException(ServerInternalError):
    pass


class DatabaseConnectionException(DatabaseException):
    pass


class SqlException(DatabaseException):
    pass


class EmptyPassword(AuthentificationException):
    pass


class PermissionsDenied(AuthentificationException):
    pass


# --


class FileException(AppException):
    pass


class EndpointBuildException(AppException):
    pass


class HTMLException(AppException):
    pass


class SqlSyntaxError(SqlException):
    pass


class IntegrityConstraintException(SqlException):
    pass


class WrongDataType(SqlException):
    pass


# --


class DumpFileException(FileException):
    pass


class EnvFileException(FileException):
    pass


class ExtractDatabaseNameException(FileException):
    pass


class DatabaseConnectionFailed(DatabaseConnectionException):
    pass


# --


class EnvVariablesException(EnvFileException):
    pass


class SqlCommandMissing(DumpFileException):
    pass


class DumpFileMissing(DumpFileException):
    pass


class ErreurFichierSqlDump(Exception):
    """Erreur qui doit être affichée lorsque le fichier DUMP à un problème"""
    pass


class ErreurConnectionBD(Exception):
    """Erreur qui doit être affichée lorsque la connection à la bd pose un problème"""
    pass