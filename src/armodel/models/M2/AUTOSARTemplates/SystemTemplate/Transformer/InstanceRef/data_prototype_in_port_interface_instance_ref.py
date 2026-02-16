"""DataPrototypeInPortInterfaceInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class DataPrototypeInPortInterfaceInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInPortInterfaceInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("abstract_base", None, False, False, PortInterface),  # abstractBase
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("root_data", None, False, False, AutosarDataPrototype),  # rootData
        ("target_data", None, False, False, DataPrototype),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceInstanceRef."""
        super().__init__()
        self.abstract_base: Optional[PortInterface] = None
        self.context_datas: list[Any] = []
        self.root_data: Optional[AutosarDataPrototype] = None
        self.target_data: DataPrototype = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeInPortInterfaceInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceInstanceRef":
        """Create DataPrototypeInPortInterfaceInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeInPortInterfaceInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeInPortInterfaceInstanceRef since parent returns ARObject
        return cast("DataPrototypeInPortInterfaceInstanceRef", obj)


class DataPrototypeInPortInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceInstanceRef = DataPrototypeInPortInterfaceInstanceRef()

    def build(self) -> DataPrototypeInPortInterfaceInstanceRef:
        """Build and return DataPrototypeInPortInterfaceInstanceRef object.

        Returns:
            DataPrototypeInPortInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
