from UI.Handlers.Handler import Handler


class SortHardwareHandler(Handler):
    def get_page(self, args):
        self.check_session()
        self.redirect_if_not_logged_in()
        interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = interactor.execute(args.get("field", "name"), args.get("sortdir", ""))
        return self.renderer.render("hardware.html", hardware=hardware, hw_sort_field=args.get("field", ""),
                                    hw_sort_dir=args.get("sortdir", ""))
