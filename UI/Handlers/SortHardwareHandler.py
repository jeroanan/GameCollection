from UI.Handlers.AuthenticatedHandler import AuthenticatedHandler


class SortHardwareHandler(AuthenticatedHandler):
    def get_page(self, args):
        super().get_page(args)
        interactor = self.interactor_factory.create("GetHardwareListInteractor")
        hardware = interactor.execute(args.get("field", "name"), args.get("sortdir", ""))
        return self.renderer.render("hardware.html", hardware=hardware, hw_sort_field=args.get("field", ""),
                                    hw_sort_dir=args.get("sortdir", ""))
