"""SwComponentPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 77)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 896)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 245)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 466)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-COMPONENT-PROTOTYPE"


    type_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TYPE-TREF": ("_POLYMORPHIC", "type_ref", ["ApplicationSwComponentType", "AtomicSwComponentType", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "EcuAbstractionSwComponentType", "NvBlockSwComponentType", "ParameterSwComponentType", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType"]),
    }


    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwComponentPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.type_ref, "SwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototype":
        """Deserialize XML element to SwComponentPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TYPE-TREF":
                setattr(obj, "type_ref", ARRef.deserialize(child))

        return obj



class SwComponentPrototypeBuilder(IdentifiableBuilder):
    """Builder for SwComponentPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwComponentPrototype = SwComponentPrototype()


    def with_type(self, value: Optional[SwComponentType]) -> "SwComponentPrototypeBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "type",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwComponentPrototype:
        """Build and return the SwComponentPrototype instance with validation."""
        self._validate_instance()
        return self._obj