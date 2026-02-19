"""EcucInstanceReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucInstanceReferenceValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[AtpFeature]
    def __init__(self) -> None:
        """Initialize EcucInstanceReferenceValue."""
        super().__init__()
        self.value: Optional[AtpFeature] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucInstanceReferenceValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucInstanceReferenceValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucInstanceReferenceValue":
        """Deserialize XML element to EcucInstanceReferenceValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucInstanceReferenceValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucInstanceReferenceValue, cls).deserialize(element)

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.value = value_value

        return obj



class EcucInstanceReferenceValueBuilder:
    """Builder for EcucInstanceReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucInstanceReferenceValue = EcucInstanceReferenceValue()

    def build(self) -> EcucInstanceReferenceValue:
        """Build and return EcucInstanceReferenceValue object.

        Returns:
            EcucInstanceReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
