import src.web.AuthenticationController as authBp
import src.web.FilmController as filmBp


def registerBluePrints(app):
    app.register_blueprint(authBp.bp)
    app.register_blueprint(filmBp.bp)

    return app