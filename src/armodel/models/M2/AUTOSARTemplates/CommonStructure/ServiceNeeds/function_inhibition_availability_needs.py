"""FunctionInhibitionAvailabilityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 318)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 751)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """AUTOSAR FunctionInhibitionAvailabilityNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    controlled_fid: Optional[FunctionInhibitionNeeds]
    def __init__(self) -> None:
        """Initialize FunctionInhibitionAvailabilityNeeds."""
        super().__init__()
        self.controlled_fid: Optional[FunctionInhibitionNeeds] = None

    def serialize(self) -> ET.Element:
        """Serialize FunctionInhibitionAvailabilityNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FunctionInhibitionAvailabilityNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize controlled_fid
        if self.controlled_fid is not None:
            serialized = ARObject._serialize_item(self.controlled_fid, "FunctionInhibitionNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLED-FID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FunctionInhibitionAvailabilityNeeds":
        """Deserialize XML element to FunctionInhibitionAvailabilityNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FunctionInhibitionAvailabilityNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FunctionInhibitionAvailabilityNeeds, cls).deserialize(element)

        # Parse controlled_fid
        child = ARObject._find_child_element(element, "CONTROLLED-FID")
        if child is not None:
            controlled_fid_value = ARObject._deserialize_by_tag(child, "FunctionInhibitionNeeds")
            obj.controlled_fid = controlled_fid_value

        return obj



class FunctionInhibitionAvailabilityNeedsBuilder:
    """Builder for FunctionInhibitionAvailabilityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FunctionInhibitionAvailabilityNeeds = FunctionInhibitionAvailabilityNeeds()

    def build(self) -> FunctionInhibitionAvailabilityNeeds:
        """Build and return FunctionInhibitionAvailabilityNeeds object.

        Returns:
            FunctionInhibitionAvailabilityNeeds instance
        """
        # TODO: Add validation
        return self._obj
