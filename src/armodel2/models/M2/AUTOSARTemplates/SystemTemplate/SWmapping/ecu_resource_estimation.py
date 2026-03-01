"""EcuResourceEstimation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 260)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_ecu_mapping import (
        SwcToEcuMapping,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class EcuResourceEstimation(ARObject):
    """AUTOSAR EcuResourceEstimation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECU-RESOURCE-ESTIMATION"


    bsw_resource: Optional[ResourceConsumption]
    ecu_instance_ref: Optional[ARRef]
    introduction: Optional[DocumentationBlock]
    rte_resource: Optional[ResourceConsumption]
    sw_comp_to_ecu_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BSW-RESOURCE": lambda obj, elem: setattr(obj, "bsw_resource", SerializationHelper.deserialize_by_tag(elem, "ResourceConsumption")),
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "RTE-RESOURCE": lambda obj, elem: setattr(obj, "rte_resource", SerializationHelper.deserialize_by_tag(elem, "ResourceConsumption")),
        "SW-COMP-TO-ECUS": lambda obj, elem: obj.sw_comp_to_ecu_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcuResourceEstimation."""
        super().__init__()
        self.bsw_resource: Optional[ResourceConsumption] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.rte_resource: Optional[ResourceConsumption] = None
        self.sw_comp_to_ecu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcuResourceEstimation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcuResourceEstimation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_resource
        if self.bsw_resource is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_resource, "ResourceConsumption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize introduction
        if self.introduction is not None:
            serialized = SerializationHelper.serialize_item(self.introduction, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTRODUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rte_resource
        if self.rte_resource is not None:
            serialized = SerializationHelper.serialize_item(self.rte_resource, "ResourceConsumption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RTE-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_comp_to_ecu_refs (list to container "SW-COMP-TO-ECU-REFS")
        if self.sw_comp_to_ecu_refs:
            wrapper = ET.Element("SW-COMP-TO-ECU-REFS")
            for item in self.sw_comp_to_ecu_refs:
                serialized = SerializationHelper.serialize_item(item, "SwcToEcuMapping")
                if serialized is not None:
                    child_elem = ET.Element("SW-COMP-TO-ECU-REF")
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
    def deserialize(cls, element: ET.Element) -> "EcuResourceEstimation":
        """Deserialize XML element to EcuResourceEstimation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuResourceEstimation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuResourceEstimation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "BSW-RESOURCE":
                setattr(obj, "bsw_resource", SerializationHelper.deserialize_by_tag(child, "ResourceConsumption"))
            elif tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "INTRODUCTION":
                setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "RTE-RESOURCE":
                setattr(obj, "rte_resource", SerializationHelper.deserialize_by_tag(child, "ResourceConsumption"))
            elif tag == "SW-COMP-TO-ECUS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sw_comp_to_ecu_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcToEcuMapping"))

        return obj



class EcuResourceEstimationBuilder(BuilderBase):
    """Builder for EcuResourceEstimation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcuResourceEstimation = EcuResourceEstimation()


    def with_bsw_resource(self, value: Optional[ResourceConsumption]) -> "EcuResourceEstimationBuilder":
        """Set bsw_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_resource = value
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "EcuResourceEstimationBuilder":
        """Set ecu_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_instance = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "EcuResourceEstimationBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_rte_resource(self, value: Optional[ResourceConsumption]) -> "EcuResourceEstimationBuilder":
        """Set rte_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rte_resource = value
        return self

    def with_sw_comp_to_ecus(self, items: list[SwcToEcuMapping]) -> "EcuResourceEstimationBuilder":
        """Set sw_comp_to_ecus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_comp_to_ecus = list(items) if items else []
        return self


    def add_sw_comp_to_ecu(self, item: SwcToEcuMapping) -> "EcuResourceEstimationBuilder":
        """Add a single item to sw_comp_to_ecus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_comp_to_ecus.append(item)
        return self

    def clear_sw_comp_to_ecus(self) -> "EcuResourceEstimationBuilder":
        """Clear all items from sw_comp_to_ecus list.

        Returns:
            self for method chaining
        """
        self._obj.sw_comp_to_ecus = []
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


    def build(self) -> EcuResourceEstimation:
        """Build and return the EcuResourceEstimation instance with validation."""
        self._validate_instance()
        pass
        return self._obj