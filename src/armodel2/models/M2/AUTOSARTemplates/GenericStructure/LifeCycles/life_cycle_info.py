"""LifeCycleInfo AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIFE-CYCLE-INFO"


    lc_object_ref: ARRef
    lc_state_ref: Optional[ARRef]
    period_begin: Optional[LifeCyclePeriod]
    period_end: Optional[LifeCyclePeriod]
    remark: Optional[DocumentationBlock]
    use_instead_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "LC-OBJECT-REF": ("_POLYMORPHIC", "lc_object_ref", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
        "LC-STATE-REF": lambda obj, elem: setattr(obj, "lc_state_ref", ARRef.deserialize(elem)),
        "PERIOD-BEGIN": lambda obj, elem: setattr(obj, "period_begin", SerializationHelper.deserialize_by_tag(elem, "LifeCyclePeriod")),
        "PERIOD-END": lambda obj, elem: setattr(obj, "period_end", SerializationHelper.deserialize_by_tag(elem, "LifeCyclePeriod")),
        "REMARK": lambda obj, elem: setattr(obj, "remark", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "USE-INSTEAD-REFS": ("_POLYMORPHIC_LIST", "use_instead_refs", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
    }


    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object_ref: ARRef = None
        self.lc_state_ref: Optional[ARRef] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_instead_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize LifeCycleInfo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleInfo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lc_object_ref
        if self.lc_object_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lc_object_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LC-OBJECT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lc_state_ref
        if self.lc_state_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lc_state_ref, "LifeCycleState")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LC-STATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period_begin
        if self.period_begin is not None:
            serialized = SerializationHelper.serialize_item(self.period_begin, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD-BEGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period_end
        if self.period_end is not None:
            serialized = SerializationHelper.serialize_item(self.period_end, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD-END")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remark
        if self.remark is not None:
            serialized = SerializationHelper.serialize_item(self.remark, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMARK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_instead_refs (list to container "USE-INSTEAD-REFS")
        if self.use_instead_refs:
            wrapper = ET.Element("USE-INSTEAD-REFS")
            for item in self.use_instead_refs:
                serialized = SerializationHelper.serialize_item(item, "Referrable")
                if serialized is not None:
                    child_elem = ET.Element("USE-INSTEAD-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfo":
        """Deserialize XML element to LifeCycleInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleInfo, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LC-OBJECT-REF":
                setattr(obj, "lc_object_ref", ARRef.deserialize(child))
            elif tag == "LC-STATE-REF":
                setattr(obj, "lc_state_ref", ARRef.deserialize(child))
            elif tag == "PERIOD-BEGIN":
                setattr(obj, "period_begin", SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod"))
            elif tag == "PERIOD-END":
                setattr(obj, "period_end", SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod"))
            elif tag == "REMARK":
                setattr(obj, "remark", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "USE-INSTEAD-REFS":
                for item_elem in child:
                    obj.use_instead_refs.append(ARRef.deserialize(item_elem))

        return obj



class LifeCycleInfoBuilder(BuilderBase):
    """Builder for LifeCycleInfo with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LifeCycleInfo = LifeCycleInfo()


    def with_lc_object(self, value: Referrable) -> "LifeCycleInfoBuilder":
        """Set lc_object attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lc_object = value
        return self

    def with_lc_state(self, value: Optional[LifeCycleState]) -> "LifeCycleInfoBuilder":
        """Set lc_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lc_state = value
        return self

    def with_period_begin(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoBuilder":
        """Set period_begin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.period_begin = value
        return self

    def with_period_end(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoBuilder":
        """Set period_end attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.period_end = value
        return self

    def with_remark(self, value: Optional[DocumentationBlock]) -> "LifeCycleInfoBuilder":
        """Set remark attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remark = value
        return self

    def with_use_insteads(self, items: list[Referrable]) -> "LifeCycleInfoBuilder":
        """Set use_insteads list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.use_insteads = list(items) if items else []
        return self


    def add_use_instead(self, item: Referrable) -> "LifeCycleInfoBuilder":
        """Add a single item to use_insteads list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.use_insteads.append(item)
        return self

    def clear_use_insteads(self) -> "LifeCycleInfoBuilder":
        """Clear all items from use_insteads list.

        Returns:
            self for method chaining
        """
        self._obj.use_insteads = []
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


    def build(self) -> LifeCycleInfo:
        """Build and return the LifeCycleInfo instance with validation."""
        self._validate_instance()
        pass
        return self._obj