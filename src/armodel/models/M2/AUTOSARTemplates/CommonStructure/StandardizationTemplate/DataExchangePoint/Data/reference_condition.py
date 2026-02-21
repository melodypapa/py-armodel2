"""ReferenceCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.reference_tailoring import (
    ReferenceTailoring,
)


class ReferenceCondition(AttributeCondition):
    """AUTOSAR ReferenceCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    reference_ref: ARRef
    def __init__(self) -> None:
        """Initialize ReferenceCondition."""
        super().__init__()
        self.reference_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize ReferenceCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReferenceCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize reference_ref
        if self.reference_ref is not None:
            serialized = ARObject._serialize_item(self.reference_ref, "ReferenceTailoring")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceCondition":
        """Deserialize XML element to ReferenceCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReferenceCondition, cls).deserialize(element)

        # Parse reference_ref
        child = ARObject._find_child_element(element, "REFERENCE-REF")
        if child is not None:
            reference_ref_value = ARRef.deserialize(child)
            obj.reference_ref = reference_ref_value

        return obj



class ReferenceConditionBuilder:
    """Builder for ReferenceCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceCondition = ReferenceCondition()

    def build(self) -> ReferenceCondition:
        """Build and return ReferenceCondition object.

        Returns:
            ReferenceCondition instance
        """
        # TODO: Add validation
        return self._obj
