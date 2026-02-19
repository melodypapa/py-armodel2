"""DiagnosticInfoType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticInfoType(DiagnosticCommonElement):
    """AUTOSAR DiagnosticInfoType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_elements: list[DiagnosticParameter]
    id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticInfoType."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticInfoType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticInfoType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_elements (list to container "DATA-ELEMENTS")
        if self.data_elements:
            wrapper = ET.Element("DATA-ELEMENTS")
            for item in self.data_elements:
                serialized = ARObject._serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize id
        if self.id is not None:
            serialized = ARObject._serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticInfoType":
        """Deserialize XML element to DiagnosticInfoType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticInfoType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticInfoType, cls).deserialize(element)

        # Parse data_elements (list from container "DATA-ELEMENTS")
        obj.data_elements = []
        container = ARObject._find_child_element(element, "DATA-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_elements.append(child_value)

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        return obj



class DiagnosticInfoTypeBuilder:
    """Builder for DiagnosticInfoType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInfoType = DiagnosticInfoType()

    def build(self) -> DiagnosticInfoType:
        """Build and return DiagnosticInfoType object.

        Returns:
            DiagnosticInfoType instance
        """
        # TODO: Add validation
        return self._obj
