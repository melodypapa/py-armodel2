"""ReferenceTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.unresolved_reference_restriction_with_severity import (
    UnresolvedReferenceRestrictionWithSeverity,
)


class ReferenceTailoring(AttributeTailoring):
    """AUTOSAR ReferenceTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_tailorings: list[ClassTailoring]
    unresolved_restriction_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ReferenceTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
        self.unresolved_restriction_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ReferenceTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReferenceTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_tailorings (list to container "TYPE-TAILORINGS")
        if self.type_tailorings:
            wrapper = ET.Element("TYPE-TAILORINGS")
            for item in self.type_tailorings:
                serialized = SerializationHelper.serialize_item(item, "ClassTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize unresolved_restriction_ref
        if self.unresolved_restriction_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unresolved_restriction_ref, "UnresolvedReferenceRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNRESOLVED-RESTRICTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceTailoring":
        """Deserialize XML element to ReferenceTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReferenceTailoring, cls).deserialize(element)

        # Parse type_tailorings (list from container "TYPE-TAILORINGS")
        obj.type_tailorings = []
        container = SerializationHelper.find_child_element(element, "TYPE-TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.type_tailorings.append(child_value)

        # Parse unresolved_restriction_ref
        child = SerializationHelper.find_child_element(element, "UNRESOLVED-RESTRICTION-REF")
        if child is not None:
            unresolved_restriction_ref_value = ARRef.deserialize(child)
            obj.unresolved_restriction_ref = unresolved_restriction_ref_value

        return obj



class ReferenceTailoringBuilder:
    """Builder for ReferenceTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceTailoring = ReferenceTailoring()

    def build(self) -> ReferenceTailoring:
        """Build and return ReferenceTailoring object.

        Returns:
            ReferenceTailoring instance
        """
        # TODO: Add validation
        return self._obj
