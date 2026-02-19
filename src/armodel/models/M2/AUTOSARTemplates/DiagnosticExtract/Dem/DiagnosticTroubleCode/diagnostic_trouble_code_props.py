"""DiagnosticTroubleCodeProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticSignificanceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticAging.diagnostic_aging import (
    DiagnosticAging,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticExtendedDataRecord.diagnostic_extended_data_record import (
    DiagnosticExtendedDataRecord,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame.diagnostic_freeze_frame import (
    DiagnosticFreezeFrame,
)


class DiagnosticTroubleCodeProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aging: Optional[DiagnosticAging]
    diagnostic_memory: Optional[Any]
    extended_datas: list[DiagnosticExtendedDataRecord]
    freeze_frames: list[DiagnosticFreezeFrame]
    immediate_nv: Optional[Boolean]
    legislated: Optional[DiagnosticDataIdentifier]
    max_number: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    significance: Optional[DiagnosticSignificanceEnum]
    snapshot: Optional[DiagnosticDataIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeProps."""
        super().__init__()
        self.aging: Optional[DiagnosticAging] = None
        self.diagnostic_memory: Optional[Any] = None
        self.extended_datas: list[DiagnosticExtendedDataRecord] = []
        self.freeze_frames: list[DiagnosticFreezeFrame] = []
        self.immediate_nv: Optional[Boolean] = None
        self.legislated: Optional[DiagnosticDataIdentifier] = None
        self.max_number: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.significance: Optional[DiagnosticSignificanceEnum] = None
        self.snapshot: Optional[DiagnosticDataIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aging
        if self.aging is not None:
            serialized = ARObject._serialize_item(self.aging, "DiagnosticAging")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_memory
        if self.diagnostic_memory is not None:
            serialized = ARObject._serialize_item(self.diagnostic_memory, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-MEMORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extended_datas (list to container "EXTENDED-DATAS")
        if self.extended_datas:
            wrapper = ET.Element("EXTENDED-DATAS")
            for item in self.extended_datas:
                serialized = ARObject._serialize_item(item, "DiagnosticExtendedDataRecord")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize freeze_frames (list to container "FREEZE-FRAMES")
        if self.freeze_frames:
            wrapper = ET.Element("FREEZE-FRAMES")
            for item in self.freeze_frames:
                serialized = ARObject._serialize_item(item, "DiagnosticFreezeFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize immediate_nv
        if self.immediate_nv is not None:
            serialized = ARObject._serialize_item(self.immediate_nv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMMEDIATE-NV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize legislated
        if self.legislated is not None:
            serialized = ARObject._serialize_item(self.legislated, "DiagnosticDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LEGISLATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number
        if self.max_number is not None:
            serialized = ARObject._serialize_item(self.max_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize significance
        if self.significance is not None:
            serialized = ARObject._serialize_item(self.significance, "DiagnosticSignificanceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNIFICANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize snapshot
        if self.snapshot is not None:
            serialized = ARObject._serialize_item(self.snapshot, "DiagnosticDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SNAPSHOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeProps":
        """Deserialize XML element to DiagnosticTroubleCodeProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeProps, cls).deserialize(element)

        # Parse aging
        child = ARObject._find_child_element(element, "AGING")
        if child is not None:
            aging_value = ARObject._deserialize_by_tag(child, "DiagnosticAging")
            obj.aging = aging_value

        # Parse diagnostic_memory
        child = ARObject._find_child_element(element, "DIAGNOSTIC-MEMORY")
        if child is not None:
            diagnostic_memory_value = child.text
            obj.diagnostic_memory = diagnostic_memory_value

        # Parse extended_datas (list from container "EXTENDED-DATAS")
        obj.extended_datas = []
        container = ARObject._find_child_element(element, "EXTENDED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.extended_datas.append(child_value)

        # Parse freeze_frames (list from container "FREEZE-FRAMES")
        obj.freeze_frames = []
        container = ARObject._find_child_element(element, "FREEZE-FRAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.freeze_frames.append(child_value)

        # Parse immediate_nv
        child = ARObject._find_child_element(element, "IMMEDIATE-NV")
        if child is not None:
            immediate_nv_value = child.text
            obj.immediate_nv = immediate_nv_value

        # Parse legislated
        child = ARObject._find_child_element(element, "LEGISLATED")
        if child is not None:
            legislated_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.legislated = legislated_value

        # Parse max_number
        child = ARObject._find_child_element(element, "MAX-NUMBER")
        if child is not None:
            max_number_value = child.text
            obj.max_number = max_number_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse significance
        child = ARObject._find_child_element(element, "SIGNIFICANCE")
        if child is not None:
            significance_value = DiagnosticSignificanceEnum.deserialize(child)
            obj.significance = significance_value

        # Parse snapshot
        child = ARObject._find_child_element(element, "SNAPSHOT")
        if child is not None:
            snapshot_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.snapshot = snapshot_value

        return obj



class DiagnosticTroubleCodePropsBuilder:
    """Builder for DiagnosticTroubleCodeProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeProps = DiagnosticTroubleCodeProps()

    def build(self) -> DiagnosticTroubleCodeProps:
        """Build and return DiagnosticTroubleCodeProps object.

        Returns:
            DiagnosticTroubleCodeProps instance
        """
        # TODO: Add validation
        return self._obj
