"""SdgTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgTailoring(RestrictionWithSeverity):
    """AUTOSAR SdgTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sdg_class: Optional[SdgClass]
    def __init__(self) -> None:
        """Initialize SdgTailoring."""
        super().__init__()
        self.sdg_class: Optional[SdgClass] = None
    def serialize(self) -> ET.Element:
        """Serialize SdgTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sdg_class
        if self.sdg_class is not None:
            serialized = ARObject._serialize_item(self.sdg_class, "SdgClass")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgTailoring":
        """Deserialize XML element to SdgTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgTailoring, cls).deserialize(element)

        # Parse sdg_class
        child = ARObject._find_child_element(element, "SDG-CLASS")
        if child is not None:
            sdg_class_value = ARObject._deserialize_by_tag(child, "SdgClass")
            obj.sdg_class = sdg_class_value

        return obj



class SdgTailoringBuilder:
    """Builder for SdgTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgTailoring = SdgTailoring()

    def build(self) -> SdgTailoring:
        """Build and return SdgTailoring object.

        Returns:
            SdgTailoring instance
        """
        # TODO: Add validation
        return self._obj
