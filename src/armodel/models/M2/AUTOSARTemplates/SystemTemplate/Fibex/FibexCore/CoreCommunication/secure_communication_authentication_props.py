"""SecureCommunicationAuthenticationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 371)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecureCommunicationAuthenticationProps(Identifiable):
    """AUTOSAR SecureCommunicationAuthenticationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auth_info_tx: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecureCommunicationAuthenticationProps."""
        super().__init__()
        self.auth_info_tx: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationAuthenticationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationAuthenticationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auth_info_tx
        if self.auth_info_tx is not None:
            serialized = ARObject._serialize_item(self.auth_info_tx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTH-INFO-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationAuthenticationProps":
        """Deserialize XML element to SecureCommunicationAuthenticationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationAuthenticationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationAuthenticationProps, cls).deserialize(element)

        # Parse auth_info_tx
        child = ARObject._find_child_element(element, "AUTH-INFO-TX")
        if child is not None:
            auth_info_tx_value = child.text
            obj.auth_info_tx = auth_info_tx_value

        return obj



class SecureCommunicationAuthenticationPropsBuilder:
    """Builder for SecureCommunicationAuthenticationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationAuthenticationProps = SecureCommunicationAuthenticationProps()

    def build(self) -> SecureCommunicationAuthenticationProps:
        """Build and return SecureCommunicationAuthenticationProps object.

        Returns:
            SecureCommunicationAuthenticationProps instance
        """
        # TODO: Add validation
        return self._obj
