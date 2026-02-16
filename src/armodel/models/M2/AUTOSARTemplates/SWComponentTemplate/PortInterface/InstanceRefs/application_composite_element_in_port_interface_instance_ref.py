"""ApplicationCompositeElementInPortInterfaceInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)


class ApplicationCompositeElementInPortInterfaceInstanceRef(ARObject):
    """AUTOSAR ApplicationCompositeElementInPortInterfaceInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, DataInterface),  # base
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("root_data", None, False, False, AutosarDataPrototype),  # rootData
        ("target_data", None, False, False, any (ApplicationComposite)),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementInPortInterfaceInstanceRef."""
        super().__init__()
        self.base: Optional[DataInterface] = None
        self.context_datas: list[Any] = []
        self.root_data: Optional[AutosarDataPrototype] = None
        self.target_data: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationCompositeElementInPortInterfaceInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeElementInPortInterfaceInstanceRef":
        """Create ApplicationCompositeElementInPortInterfaceInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationCompositeElementInPortInterfaceInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationCompositeElementInPortInterfaceInstanceRef since parent returns ARObject
        return cast("ApplicationCompositeElementInPortInterfaceInstanceRef", obj)


class ApplicationCompositeElementInPortInterfaceInstanceRefBuilder:
    """Builder for ApplicationCompositeElementInPortInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeElementInPortInterfaceInstanceRef = ApplicationCompositeElementInPortInterfaceInstanceRef()

    def build(self) -> ApplicationCompositeElementInPortInterfaceInstanceRef:
        """Build and return ApplicationCompositeElementInPortInterfaceInstanceRef object.

        Returns:
            ApplicationCompositeElementInPortInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
