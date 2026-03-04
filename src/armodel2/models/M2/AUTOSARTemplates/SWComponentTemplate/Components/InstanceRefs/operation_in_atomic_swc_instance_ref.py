"""OperationInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 946)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
        AtomicSwComponentType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
        ClientServerOperation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class OperationInAtomicSwcInstanceRef(ARObject, ABC):
    """AUTOSAR OperationInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base_ref: Optional[ARRef]
    context_port_ref: Optional[ARRef]
    target_operation_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": ("_POLYMORPHIC", "base_ref", ["ApplicationSwComponentType", "ComplexDeviceDriverSwComponentType", "EcuAbstractionSwComponentType", "NvBlockSwComponentType", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType"]),
        "CONTEXT-PORT-REF": ("_POLYMORPHIC", "context_port_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
        "TARGET-OPERATION-REF": lambda obj, elem: setattr(obj, "target_operation_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize OperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_port_ref: Optional[ARRef] = None
        self.target_operation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize OperationInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(OperationInAtomicSwcInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "AtomicSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_operation_ref
        if self.target_operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInAtomicSwcInstanceRef":
        """Deserialize XML element to OperationInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OperationInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(OperationInAtomicSwcInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-PORT-REF":
                setattr(obj, "context_port_ref", ARRef.deserialize(child))
            elif tag == "TARGET-OPERATION-REF":
                setattr(obj, "target_operation_ref", ARRef.deserialize(child))

        return obj



class OperationInAtomicSwcInstanceRefBuilder(BuilderBase, ABC):
    """Builder for OperationInAtomicSwcInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: OperationInAtomicSwcInstanceRef = OperationInAtomicSwcInstanceRef()


    def with_base(self, value: Optional[AtomicSwComponentType]) -> "OperationInAtomicSwcInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context_port(self, value: Optional[PortPrototype]) -> "OperationInAtomicSwcInstanceRefBuilder":
        """Set context_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_port = value
        return self

    def with_target_operation(self, value: Optional[ClientServerOperation]) -> "OperationInAtomicSwcInstanceRefBuilder":
        """Set target_operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_operation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "contextPort",
        "targetOperation",
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
    def build(self) -> OperationInAtomicSwcInstanceRef:
        """Build and return the OperationInAtomicSwcInstanceRef instance (abstract)."""
        raise NotImplementedError