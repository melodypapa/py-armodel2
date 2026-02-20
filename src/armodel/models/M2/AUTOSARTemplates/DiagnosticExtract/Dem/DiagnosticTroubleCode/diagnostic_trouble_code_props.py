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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    aging_ref: Optional[ARRef]
    diagnostic_memory_ref: Optional[Any]
    extended_data_refs: list[ARRef]
    freeze_frame_refs: list[ARRef]
    immediate_nv: Optional[Boolean]
    legislated_ref: Optional[ARRef]
    max_number: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    significance: Optional[DiagnosticSignificanceEnum]
    snapshot_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeProps."""
        super().__init__()
        self.aging_ref: Optional[ARRef] = None
        self.diagnostic_memory_ref: Optional[Any] = None
        self.extended_data_refs: list[ARRef] = []
        self.freeze_frame_refs: list[ARRef] = []
        self.immediate_nv: Optional[Boolean] = None
        self.legislated_ref: Optional[ARRef] = None
        self.max_number: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.significance: Optional[DiagnosticSignificanceEnum] = None
        self.snapshot_ref: Optional[ARRef] = None

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

        # Serialize aging_ref
        if self.aging_ref is not None:
            serialized = ARObject._serialize_item(self.aging_ref, "DiagnosticAging")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_memory_ref
        if self.diagnostic_memory_ref is not None:
            serialized = ARObject._serialize_item(self.diagnostic_memory_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-MEMORY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extended_data_refs (list to container "EXTENDED-DATA-REFS")
        if self.extended_data_refs:
            wrapper = ET.Element("EXTENDED-DATA-REFS")
            for item in self.extended_data_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticExtendedDataRecord")
                if serialized is not None:
                    child_elem = ET.Element("EXTENDED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize freeze_frame_refs (list to container "FREEZE-FRAME-REFS")
        if self.freeze_frame_refs:
            wrapper = ET.Element("FREEZE-FRAME-REFS")
            for item in self.freeze_frame_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticFreezeFrame")
                if serialized is not None:
                    child_elem = ET.Element("FREEZE-FRAME-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Serialize legislated_ref
        if self.legislated_ref is not None:
            serialized = ARObject._serialize_item(self.legislated_ref, "DiagnosticDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LEGISLATED-REF")
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

        # Serialize snapshot_ref
        if self.snapshot_ref is not None:
            serialized = ARObject._serialize_item(self.snapshot_ref, "DiagnosticDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SNAPSHOT-REF")
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

        # Parse aging_ref
        child = ARObject._find_child_element(element, "AGING-REF")
        if child is not None:
            aging_ref_value = ARRef.deserialize(child)
            obj.aging_ref = aging_ref_value

        # Parse diagnostic_memory_ref
        child = ARObject._find_child_element(element, "DIAGNOSTIC-MEMORY-REF")
        if child is not None:
            diagnostic_memory_ref_value = ARRef.deserialize(child)
            obj.diagnostic_memory_ref = diagnostic_memory_ref_value

        # Parse extended_data_refs (list from container "EXTENDED-DATA-REFS")
        obj.extended_data_refs = []
        container = ARObject._find_child_element(element, "EXTENDED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.extended_data_refs.append(child_value)

        # Parse freeze_frame_refs (list from container "FREEZE-FRAME-REFS")
        obj.freeze_frame_refs = []
        container = ARObject._find_child_element(element, "FREEZE-FRAME-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.freeze_frame_refs.append(child_value)

        # Parse immediate_nv
        child = ARObject._find_child_element(element, "IMMEDIATE-NV")
        if child is not None:
            immediate_nv_value = child.text
            obj.immediate_nv = immediate_nv_value

        # Parse legislated_ref
        child = ARObject._find_child_element(element, "LEGISLATED-REF")
        if child is not None:
            legislated_ref_value = ARRef.deserialize(child)
            obj.legislated_ref = legislated_ref_value

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

        # Parse snapshot_ref
        child = ARObject._find_child_element(element, "SNAPSHOT-REF")
        if child is not None:
            snapshot_ref_value = ARRef.deserialize(child)
            obj.snapshot_ref = snapshot_ref_value

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
