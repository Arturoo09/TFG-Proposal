import sentry_sdk
from config import SentryConst

class Sentry:
    def __init__(self) -> None:
        self.init(SentryConst.SENTRY_DNS, SentryConst.SENTRY_ENV)
    
    def init(self, dns, env) -> None:
        """Inicializar entorno 

        Args:
            dns (str): url del sentry
            env (str): nombre del entorno
        """
        if not dns and not env:
            return
        
        sentry_sdk.init(dns=dns, environment=env)
        return
    
    def flush(self):
        sentry_sdk.flush() 
        
    def capture_sentry(self, exception: Exception, tags: dict = None): 
        """Captura la excepción del codigo

        Args:
            exception (Exception): Excepción a capturar.
            tags (dict, optional): tags definidas en el codigo. Defaults to None.
        """
        with sentry_sdk.configure_scope() as scope:
            if tags:
                for key, value in tags.items():
                    scope.set_tag(key, value)
            
            sentry_sdk.capture_exception(exception)