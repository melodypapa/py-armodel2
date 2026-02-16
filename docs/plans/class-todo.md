Let us analyze the  `demos/arxml/AUTOSAR_Datatypes.arxml` and `docs/json/hierarchy.json`

1. Collect all the related classes and their parent class list as a table in the `docs/reports/class-todo-items.md` until the parent class is already ArObject.
2. Base on `docs/reports/class-todo-items.md` and `docs/json/mapping.json`
  1. Update these clasess and their parent class hierarcy in code base according to `docs/json/hierarchy.json`.
  2. Update the memeber list of these classes and their parent in code base according to `docs/json/packages`.