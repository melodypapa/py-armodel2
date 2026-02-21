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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    dtc_refs: list[ARRef]
    group_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeGroup."""
        super().__init__()
        self.dtc_refs: list[ARRef] = []
        self.group_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dtc_refs (list to container "DTC-REFS")
        if self.dtc_refs:
            wrapper = ET.Element("DTC-REFS")
            for item in self.dtc_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticTroubleCode")
                if serialized is not None:
                    child_elem = ET.Element("DTC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize group_number
        if self.group_number is not None:
            serialized = SerializationHelper.serialize_item(self.group_number, "PositiveInteger")
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

        # Parse dtc_refs (list from container "DTC-REFS")
        obj.dtc_refs = []
        container = SerializationHelper.find_child_element(element, "DTC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dtc_refs.append(child_value)

        # Parse group_number
        child = SerializationHelper.find_child_element(element, "GROUP-NUMBER")
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
