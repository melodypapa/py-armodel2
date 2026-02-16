"""DataPrototypeInPortInterfaceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR DataPrototypeInPortInterfaceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_prototype_in": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # dataPrototypeIn
    }

    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceRef."""
        super().__init__()
        self.data_prototype_in: Optional[DataPrototype] = None


class DataPrototypeInPortInterfaceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceRef = DataPrototypeInPortInterfaceRef()

    def build(self) -> DataPrototypeInPortInterfaceRef:
        """Build and return DataPrototypeInPortInterfaceRef object.

        Returns:
            DataPrototypeInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
