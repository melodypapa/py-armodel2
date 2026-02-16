"""MacSecProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_local_kay_props import (
    MacSecLocalKayProps,
)


class MacSecProps(ARObject):
    """AUTOSAR MacSecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("auto_start", None, True, False, None),  # autoStart
        ("mac_sec_kay", None, False, False, MacSecLocalKayProps),  # macSecKay
        ("on_fail", None, True, False, None),  # onFail
        ("sak_rekey_time", None, True, False, None),  # sakRekeyTime
    ]

    def __init__(self) -> None:
        """Initialize MacSecProps."""
        super().__init__()
        self.auto_start: Optional[Boolean] = None
        self.mac_sec_kay: Optional[MacSecLocalKayProps] = None
        self.on_fail: Optional[TimeValue] = None
        self.sak_rekey_time: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecProps":
        """Create MacSecProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecProps since parent returns ARObject
        return cast("MacSecProps", obj)


class MacSecPropsBuilder:
    """Builder for MacSecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecProps = MacSecProps()

    def build(self) -> MacSecProps:
        """Build and return MacSecProps object.

        Returns:
            MacSecProps instance
        """
        # TODO: Add validation
        return self._obj
