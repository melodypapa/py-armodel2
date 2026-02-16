"""SystemSignal AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class SystemSignal(ARElement):
    """AUTOSAR SystemSignal."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamic_length", None, True, False, None),  # dynamicLength
        ("physical_props", None, False, False, SwDataDefProps),  # physicalProps
    ]

    def __init__(self) -> None:
        """Initialize SystemSignal."""
        super().__init__()
        self.dynamic_length: Optional[Boolean] = None
        self.physical_props: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SystemSignal to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignal":
        """Create SystemSignal from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SystemSignal instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SystemSignal since parent returns ARObject
        return cast("SystemSignal", obj)


class SystemSignalBuilder:
    """Builder for SystemSignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignal = SystemSignal()

    def build(self) -> SystemSignal:
        """Build and return SystemSignal object.

        Returns:
            SystemSignal instance
        """
        # TODO: Add validation
        return self._obj
