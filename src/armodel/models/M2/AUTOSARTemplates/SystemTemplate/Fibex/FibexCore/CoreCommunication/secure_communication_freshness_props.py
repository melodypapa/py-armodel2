"""SecureCommunicationFreshnessProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SecureCommunicationFreshnessProps(Identifiable):
    """AUTOSAR SecureCommunicationFreshnessProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    freshness: Optional[PositiveInteger]
    freshness_value: Optional[PositiveInteger]
    use_freshness: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SecureCommunicationFreshnessProps."""
        super().__init__()
        self.freshness: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.use_freshness: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationFreshnessProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationFreshnessProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize freshness
        if self.freshness is not None:
            serialized = ARObject._serialize_item(self.freshness, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freshness_value
        if self.freshness_value is not None:
            serialized = ARObject._serialize_item(self.freshness_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_freshness
        if self.use_freshness is not None:
            serialized = ARObject._serialize_item(self.use_freshness, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-FRESHNESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationFreshnessProps":
        """Deserialize XML element to SecureCommunicationFreshnessProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationFreshnessProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationFreshnessProps, cls).deserialize(element)

        # Parse freshness
        child = ARObject._find_child_element(element, "FRESHNESS")
        if child is not None:
            freshness_value = child.text
            obj.freshness = freshness_value

        # Parse freshness_value
        child = ARObject._find_child_element(element, "FRESHNESS-VALUE")
        if child is not None:
            freshness_value_value = child.text
            obj.freshness_value = freshness_value_value

        # Parse use_freshness
        child = ARObject._find_child_element(element, "USE-FRESHNESS")
        if child is not None:
            use_freshness_value = child.text
            obj.use_freshness = use_freshness_value

        return obj



class SecureCommunicationFreshnessPropsBuilder:
    """Builder for SecureCommunicationFreshnessProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationFreshnessProps = SecureCommunicationFreshnessProps()

    def build(self) -> SecureCommunicationFreshnessProps:
        """Build and return SecureCommunicationFreshnessProps object.

        Returns:
            SecureCommunicationFreshnessProps instance
        """
        # TODO: Add validation
        return self._obj
