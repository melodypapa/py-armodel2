"""EcucDefinitionElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 45)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucScopeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_validation_condition import (
        EcucValidationCondition,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDefinitionElement(Identifiable, ABC):
    """AUTOSAR EcucDefinitionElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    ecuc_cond: Optional[Any]
    ecuc_validations: list[EcucValidationCondition]
    lower_multiplicity: Optional[PositiveInteger]
    related_trace_ref: Optional[ARRef]
    scope: Optional[EcucScopeEnum]
    upper_multiplicity: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ECUC-COND": lambda obj, elem: setattr(obj, "ecuc_cond", SerializationHelper.deserialize_by_tag(elem, "any (EcucCondition)")),
        "ECUC-VALIDATIONS": lambda obj, elem: obj.ecuc_validations.append(SerializationHelper.deserialize_by_tag(elem, "EcucValidationCondition")),
        "LOWER-MULTIPLICITY": lambda obj, elem: setattr(obj, "lower_multiplicity", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RELATED-TRACE-REF": ("_POLYMORPHIC", "related_trace_ref", ["AgeConstraint", "ArbitraryEventTriggering", "BurstPatternEventTriggering", "ConcretePatternEventTriggering", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "LatencyTimingConstraint", "OffsetTimingConstraint", "PeriodicEventTriggering", "SporadicEventTriggering", "StructuredReq", "SynchronizationPointConstraint", "TimingConstraint", "TraceableTable", "TraceableText"]),
        "SCOPE": lambda obj, elem: setattr(obj, "scope", EcucScopeEnum.deserialize(elem)),
        "UPPER-MULTIPLICITY": lambda obj, elem: setattr(obj, "upper_multiplicity", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize EcucDefinitionElement."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.ecuc_validations: list[EcucValidationCondition] = []
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.related_trace_ref: Optional[ARRef] = None
        self.scope: Optional[EcucScopeEnum] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucDefinitionElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDefinitionElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_cond
        if self.ecuc_cond is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_cond, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-COND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_validations (list to container "ECUC-VALIDATIONS")
        if self.ecuc_validations:
            wrapper = ET.Element("ECUC-VALIDATIONS")
            for item in self.ecuc_validations:
                serialized = SerializationHelper.serialize_item(item, "EcucValidationCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lower_multiplicity
        if self.lower_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.lower_multiplicity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize related_trace_ref
        if self.related_trace_ref is not None:
            serialized = SerializationHelper.serialize_item(self.related_trace_ref, "Traceable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELATED-TRACE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scope
        if self.scope is not None:
            serialized = SerializationHelper.serialize_item(self.scope, "EcucScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_multiplicity
        if self.upper_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.upper_multiplicity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionElement":
        """Deserialize XML element to EcucDefinitionElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDefinitionElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDefinitionElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECUC-COND":
                setattr(obj, "ecuc_cond", SerializationHelper.deserialize_by_tag(child, "any (EcucCondition)"))
            elif tag == "ECUC-VALIDATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ecuc_validations.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucValidationCondition"))
            elif tag == "LOWER-MULTIPLICITY":
                setattr(obj, "lower_multiplicity", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RELATED-TRACE-REF":
                setattr(obj, "related_trace_ref", ARRef.deserialize(child))
            elif tag == "SCOPE":
                setattr(obj, "scope", EcucScopeEnum.deserialize(child))
            elif tag == "UPPER-MULTIPLICITY":
                setattr(obj, "upper_multiplicity", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class EcucDefinitionElementBuilder(IdentifiableBuilder):
    """Builder for EcucDefinitionElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDefinitionElement = EcucDefinitionElement()


    def with_ecuc_cond(self, value: Optional[Any]) -> "EcucDefinitionElementBuilder":
        """Set ecuc_cond attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ecuc_cond' is required and cannot be None")
        self._obj.ecuc_cond = value
        return self

    def with_ecuc_validations(self, items: list[EcucValidationCondition]) -> "EcucDefinitionElementBuilder":
        """Set ecuc_validations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations = list(items) if items else []
        return self

    def with_lower_multiplicity(self, value: Optional[PositiveInteger]) -> "EcucDefinitionElementBuilder":
        """Set lower_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'lower_multiplicity' is required and cannot be None")
        self._obj.lower_multiplicity = value
        return self

    def with_related_trace(self, value: Optional[Traceable]) -> "EcucDefinitionElementBuilder":
        """Set related_trace attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'related_trace' is required and cannot be None")
        self._obj.related_trace = value
        return self

    def with_scope(self, value: Optional[EcucScopeEnum]) -> "EcucDefinitionElementBuilder":
        """Set scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'scope' is required and cannot be None")
        self._obj.scope = value
        return self

    def with_upper_multiplicity(self, value: Optional[Boolean]) -> "EcucDefinitionElementBuilder":
        """Set upper_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'upper_multiplicity' is required and cannot be None")
        self._obj.upper_multiplicity = value
        return self


    def add_ecuc_validation(self, item: EcucValidationCondition) -> "EcucDefinitionElementBuilder":
        """Add a single item to ecuc_validations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations.append(item)
        return self

    def clear_ecuc_validations(self) -> "EcucDefinitionElementBuilder":
        """Clear all items from ecuc_validations list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_validations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ecucCond",
        "ecucValidation",
        "lowerMultiplicity",
        "relatedTrace",
        "scope",
        "upperMultiplicity",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> EcucDefinitionElement:
        """Build and return the EcucDefinitionElement instance (abstract)."""
        raise NotImplementedError