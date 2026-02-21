"""ConstraintTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 117)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class ConstraintTailoring(RestrictionWithSeverity):
    """AUTOSAR ConstraintTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    constraint_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ConstraintTailoring."""
        super().__init__()
        self.constraint_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ConstraintTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstraintTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constraint_ref
        if self.constraint_ref is not None:
            serialized = ARObject._serialize_item(self.constraint_ref, "TraceableText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSTRAINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstraintTailoring":
        """Deserialize XML element to ConstraintTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstraintTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstraintTailoring, cls).deserialize(element)

        # Parse constraint_ref
        child = ARObject._find_child_element(element, "CONSTRAINT-REF")
        if child is not None:
            constraint_ref_value = ARRef.deserialize(child)
            obj.constraint_ref = constraint_ref_value

        return obj



class ConstraintTailoringBuilder:
    """Builder for ConstraintTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstraintTailoring = ConstraintTailoring()

    def build(self) -> ConstraintTailoring:
        """Build and return ConstraintTailoring object.

        Returns:
            ConstraintTailoring instance
        """
        # TODO: Add validation
        return self._obj
