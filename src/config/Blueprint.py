import src.web.AuthenticationController as bps


def registerBluePrints(app):
    app.register_blueprint(bps.bp)

    return app