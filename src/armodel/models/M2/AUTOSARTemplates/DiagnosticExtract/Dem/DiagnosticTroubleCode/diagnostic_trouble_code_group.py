"""DiagnosticTroubleCodeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtcs: list[DiagnosticTroubleCode]
    group_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeGroup."""
        super().__init__()
        self.dtcs: list[DiagnosticTroubleCode] = []
        self.group_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dtcs (list to container "DTCS")
        if self.dtcs:
            wrapper = ET.Element("DTCS")
            for item in self.dtcs:
                serialized = ARObject._serialize_item(item, "DiagnosticTroubleCode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize group_number
        if self.group_number is not None:
            serialized = ARObject._serialize_item(self.group_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GROUP-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeGroup":
        """Deserialize XML element to DiagnosticTroubleCodeGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeGroup, cls).deserialize(element)

        # Parse dtcs (list from container "DTCS")
        obj.dtcs = []
        container = ARObject._find_child_element(element, "DTCS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dtcs.append(child_value)

        # Parse group_number
        child = ARObject._find_child_element(element, "GROUP-NUMBER")
        if child is not None:
            group_number_value = child.text
            obj.group_number = group_number_value

        return obj



class DiagnosticTroubleCodeGroupBuilder:
    """Builder for DiagnosticTroubleCodeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeGroup = DiagnosticTroubleCodeGroup()

    def build(self) -> DiagnosticTroubleCodeGroup:
        """Build and return DiagnosticTroubleCodeGroup object.

        Returns:
            DiagnosticTroubleCodeGroup instance
        """
        # TODO: Add validation
        return self._obj
