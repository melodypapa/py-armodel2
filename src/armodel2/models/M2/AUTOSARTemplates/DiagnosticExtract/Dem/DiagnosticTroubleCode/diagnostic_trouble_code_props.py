"""DiagnosticTroubleCodeProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticSignificanceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticAging.diagnostic_aging import (
    DiagnosticAging,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticExtendedDataRecord.diagnostic_extended_data_record import (
    DiagnosticExtendedDataRecord,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame.diagnostic_freeze_frame import (
    DiagnosticFreezeFrame,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticTroubleCodeProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-TROUBLE-CODE-PROPS"


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
    _DESERIALIZE_DISPATCH = {
        "AGING-REF": lambda obj, elem: setattr(obj, "aging_ref", ARRef.deserialize(elem)),
        "DIAGNOSTIC-MEMORY-REF": lambda obj, elem: setattr(obj, "diagnostic_memory_ref", ARRef.deserialize(elem)),
        "EXTENDED-DATAS": lambda obj, elem: obj.extended_data_refs.append(ARRef.deserialize(elem)),
        "FREEZE-FRAMES": lambda obj, elem: obj.freeze_frame_refs.append(ARRef.deserialize(elem)),
        "IMMEDIATE-NV": lambda obj, elem: setattr(obj, "immediate_nv", elem.text),
        "LEGISLATED-REF": lambda obj, elem: setattr(obj, "legislated_ref", ARRef.deserialize(elem)),
        "MAX-NUMBER": lambda obj, elem: setattr(obj, "max_number", elem.text),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", elem.text),
        "SIGNIFICANCE": lambda obj, elem: setattr(obj, "significance", DiagnosticSignificanceEnum.deserialize(elem)),
        "SNAPSHOT-REF": lambda obj, elem: setattr(obj, "snapshot_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aging_ref
        if self.aging_ref is not None:
            serialized = SerializationHelper.serialize_item(self.aging_ref, "DiagnosticAging")
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
            serialized = SerializationHelper.serialize_item(self.diagnostic_memory_ref, "Any")
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
                serialized = SerializationHelper.serialize_item(item, "DiagnosticExtendedDataRecord")
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
                serialized = SerializationHelper.serialize_item(item, "DiagnosticFreezeFrame")
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
            serialized = SerializationHelper.serialize_item(self.immediate_nv, "Boolean")
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
            serialized = SerializationHelper.serialize_item(self.legislated_ref, "DiagnosticDataIdentifier")
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
            serialized = SerializationHelper.serialize_item(self.max_number, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.significance, "DiagnosticSignificanceEnum")
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
            serialized = SerializationHelper.serialize_item(self.snapshot_ref, "DiagnosticDataIdentifier")
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
        child = SerializationHelper.find_child_element(element, "AGING-REF")
        if child is not None:
            aging_ref_value = ARRef.deserialize(child)
            obj.aging_ref = aging_ref_value

        # Parse diagnostic_memory_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-MEMORY-REF")
        if child is not None:
            diagnostic_memory_ref_value = ARRef.deserialize(child)
            obj.diagnostic_memory_ref = diagnostic_memory_ref_value

        # Parse extended_data_refs (list from container "EXTENDED-DATA-REFS")
        obj.extended_data_refs = []
        container = SerializationHelper.find_child_element(element, "EXTENDED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.extended_data_refs.append(child_value)

        # Parse freeze_frame_refs (list from container "FREEZE-FRAME-REFS")
        obj.freeze_frame_refs = []
        container = SerializationHelper.find_child_element(element, "FREEZE-FRAME-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.freeze_frame_refs.append(child_value)

        # Parse immediate_nv
        child = SerializationHelper.find_child_element(element, "IMMEDIATE-NV")
        if child is not None:
            immediate_nv_value = child.text
            obj.immediate_nv = immediate_nv_value

        # Parse legislated_ref
        child = SerializationHelper.find_child_element(element, "LEGISLATED-REF")
        if child is not None:
            legislated_ref_value = ARRef.deserialize(child)
            obj.legislated_ref = legislated_ref_value

        # Parse max_number
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER")
        if child is not None:
            max_number_value = child.text
            obj.max_number = max_number_value

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse significance
        child = SerializationHelper.find_child_element(element, "SIGNIFICANCE")
        if child is not None:
            significance_value = DiagnosticSignificanceEnum.deserialize(child)
            obj.significance = significance_value

        # Parse snapshot_ref
        child = SerializationHelper.find_child_element(element, "SNAPSHOT-REF")
        if child is not None:
            snapshot_ref_value = ARRef.deserialize(child)
            obj.snapshot_ref = snapshot_ref_value

        return obj



class DiagnosticTroubleCodePropsBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticTroubleCodeProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticTroubleCodeProps = DiagnosticTroubleCodeProps()


    def with_aging(self, value: Optional[DiagnosticAging]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set aging attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aging = value
        return self

    def with_diagnostic_memory(self, value: Optional[any (DiagnosticMemory)]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set diagnostic_memory attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_memory = value
        return self

    def with_extended_datas(self, items: list[DiagnosticExtendedDataRecord]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set extended_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.extended_datas = list(items) if items else []
        return self

    def with_freeze_frames(self, items: list[DiagnosticFreezeFrame]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set freeze_frames list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.freeze_frames = list(items) if items else []
        return self

    def with_immediate_nv(self, value: Optional[Boolean]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set immediate_nv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.immediate_nv = value
        return self

    def with_legislated(self, value: Optional[DiagnosticDataIdentifier]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set legislated attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.legislated = value
        return self

    def with_max_number(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set max_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_significance(self, value: Optional[DiagnosticSignificanceEnum]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set significance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.significance = value
        return self

    def with_snapshot(self, value: Optional[DiagnosticDataIdentifier]) -> "DiagnosticTroubleCodePropsBuilder":
        """Set snapshot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.snapshot = value
        return self


    def add_extended_data(self, item: DiagnosticExtendedDataRecord) -> "DiagnosticTroubleCodePropsBuilder":
        """Add a single item to extended_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.extended_datas.append(item)
        return self

    def clear_extended_datas(self) -> "DiagnosticTroubleCodePropsBuilder":
        """Clear all items from extended_datas list.

        Returns:
            self for method chaining
        """
        self._obj.extended_datas = []
        return self

    def add_freeze_frame(self, item: DiagnosticFreezeFrame) -> "DiagnosticTroubleCodePropsBuilder":
        """Add a single item to freeze_frames list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.freeze_frames.append(item)
        return self

    def clear_freeze_frames(self) -> "DiagnosticTroubleCodePropsBuilder":
        """Clear all items from freeze_frames list.

        Returns:
            self for method chaining
        """
        self._obj.freeze_frames = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DiagnosticTroubleCodeProps:
        """Build and return the DiagnosticTroubleCodeProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj