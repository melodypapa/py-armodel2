"""UserDefinedPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 345)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class UserDefinedPdu(Pdu):
    """AUTOSAR UserDefinedPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cdd_type: Optional[String]
    def __init__(self) -> None:
        """Initialize UserDefinedPdu."""
        super().__init__()
        self.cdd_type: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize UserDefinedPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cdd_type
        if self.cdd_type is not None:
            serialized = ARObject._serialize_item(self.cdd_type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CDD-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedPdu":
        """Deserialize XML element to UserDefinedPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UserDefinedPdu, cls).deserialize(element)

        # Parse cdd_type
        child = ARObject._find_child_element(element, "CDD-TYPE")
        if child is not None:
            cdd_type_value = child.text
            obj.cdd_type = cdd_type_value

        return obj



class UserDefinedPduBuilder:
    """Builder for UserDefinedPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedPdu = UserDefinedPdu()

    def build(self) -> UserDefinedPdu:
        """Build and return UserDefinedPdu object.

        Returns:
            UserDefinedPdu instance
        """
        # TODO: Add validation
        return self._obj
