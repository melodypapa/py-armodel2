"""AtpPrototype AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_type import (
    AtpType,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AtpPrototype(Identifiable, ABC):
    """AUTOSAR AtpPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_type_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "ATP-TYPE-REF": ("_POLYMORPHIC", "atp_type_ref", ["ApplicationArrayDataType", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationSwComponentType", "AutosarDataType", "ClientServerInterface", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "EcuAbstractionSwComponentType", "ImplementationDataType", "ModeDeclarationGroup", "ModeDeclarationMappingSet", "ModeSwitchInterface", "NvBlockSwComponentType", "NvDataInterface", "ParameterInterface", "ParameterSwComponentType", "PortInterface", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType", "SwComponentType", "TriggerInterface"]),
    }


    def __init__(self) -> None:
        """Initialize AtpPrototype."""
        super().__init__()
        self.atp_type_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize AtpPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize atp_type_ref
        if self.atp_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_type_ref, "AtpType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpPrototype":
        """Deserialize XML element to AtpPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ATP-TYPE-REF":
                setattr(obj, "atp_type_ref", ARRef.deserialize(child))

        return obj



class AtpPrototypeBuilder(IdentifiableBuilder):
    """Builder for AtpPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AtpPrototype = AtpPrototype()


    def with_atp_type(self, value: AtpType) -> "AtpPrototypeBuilder":
        """Set atp_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.atp_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "atpType",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "atpType", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'atpType' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'atpType' is None", UserWarning)


    @abstractmethod
    def build(self) -> AtpPrototype:
        """Build and return the AtpPrototype instance (abstract)."""
        raise NotImplementedError