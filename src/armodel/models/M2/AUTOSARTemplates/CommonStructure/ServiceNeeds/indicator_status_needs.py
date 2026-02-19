"""IndicatorStatusNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 766)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator import (
    DiagnosticIndicatorTypeEnum,
)


class IndicatorStatusNeeds(ServiceNeeds):
    """AUTOSAR IndicatorStatusNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_enum: Optional[DiagnosticIndicatorTypeEnum]
    def __init__(self) -> None:
        """Initialize IndicatorStatusNeeds."""
        super().__init__()
        self.type_enum: Optional[DiagnosticIndicatorTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize IndicatorStatusNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IndicatorStatusNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_enum
        if self.type_enum is not None:
            serialized = ARObject._serialize_item(self.type_enum, "DiagnosticIndicatorTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndicatorStatusNeeds":
        """Deserialize XML element to IndicatorStatusNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndicatorStatusNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IndicatorStatusNeeds, cls).deserialize(element)

        # Parse type_enum
        child = ARObject._find_child_element(element, "TYPE-ENUM")
        if child is not None:
            type_enum_value = DiagnosticIndicatorTypeEnum.deserialize(child)
            obj.type_enum = type_enum_value

        return obj



class IndicatorStatusNeedsBuilder:
    """Builder for IndicatorStatusNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndicatorStatusNeeds = IndicatorStatusNeeds()

    def build(self) -> IndicatorStatusNeeds:
        """Build and return IndicatorStatusNeeds object.

        Returns:
            IndicatorStatusNeeds instance
        """
        # TODO: Add validation
        return self._obj
