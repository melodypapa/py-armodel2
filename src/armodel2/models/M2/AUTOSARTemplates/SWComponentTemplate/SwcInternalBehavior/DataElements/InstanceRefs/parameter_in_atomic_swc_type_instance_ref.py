"""ParameterInAtomicSWCTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 319)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
        ApplicationCompositeElementDataPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
        AtomicSwComponentType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
        DataPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ParameterInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR ParameterInAtomicSWCTypeInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_data_prototype_refs: list[ARRef]
    port_prototype_ref: Optional[ARRef]
    root_parameter_data_prototype_ref: Optional[ARRef]
    target_data_prototype_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": ("_POLYMORPHIC", "base_ref", ["ApplicationSwComponentType", "ComplexDeviceDriverSwComponentType", "EcuAbstractionSwComponentType", "NvBlockSwComponentType", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType"]),
        "CONTEXT-DATA-PROTOTYPE-REFS": ("_POLYMORPHIC_LIST", "context_data_prototype_refs", ["ApplicationArrayElement", "ApplicationRecordElement"]),
        "PORT-PROTOTYPE-REF": ("_POLYMORPHIC", "port_prototype_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
        "ROOT-PARAMETER-DATA-PROTOTYPE-REF": ("_POLYMORPHIC", "root_parameter_data_prototype_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "TARGET-DATA-PROTOTYPE-REF": ("_POLYMORPHIC", "target_data_prototype_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize ParameterInAtomicSWCTypeInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_data_prototype_refs: list[ARRef] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_parameter_data_prototype_ref: Optional[ARRef] = None
        self.target_data_prototype_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ParameterInAtomicSWCTypeInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterInAtomicSWCTypeInstanceRef, self).serialize()

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

        # Serialize context_data_prototype_refs (list to container "CONTEXT-DATA-PROTOTYPE-REFS")
        if self.context_data_prototype_refs:
            wrapper = ET.Element("CONTEXT-DATA-PROTOTYPE-REFS")
            for item in self.context_data_prototype_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationCompositeElementDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-DATA-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_prototype_ref
        if self.port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_prototype_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_parameter_data_prototype_ref
        if self.root_parameter_data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_parameter_data_prototype_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-PARAMETER-DATA-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_prototype_ref
        if self.target_data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_prototype_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterInAtomicSWCTypeInstanceRef":
        """Deserialize XML element to ParameterInAtomicSWCTypeInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterInAtomicSWCTypeInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterInAtomicSWCTypeInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-DATA-PROTOTYPE-REFS":
                for item_elem in child:
                    obj.context_data_prototype_refs.append(ARRef.deserialize(item_elem))
            elif tag == "PORT-PROTOTYPE-REF":
                setattr(obj, "port_prototype_ref", ARRef.deserialize(child))
            elif tag == "ROOT-PARAMETER-DATA-PROTOTYPE-REF":
                setattr(obj, "root_parameter_data_prototype_ref", ARRef.deserialize(child))
            elif tag == "TARGET-DATA-PROTOTYPE-REF":
                setattr(obj, "target_data_prototype_ref", ARRef.deserialize(child))

        return obj



class ParameterInAtomicSWCTypeInstanceRefBuilder(BuilderBase):
    """Builder for ParameterInAtomicSWCTypeInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ParameterInAtomicSWCTypeInstanceRef = ParameterInAtomicSWCTypeInstanceRef()


    def with_base(self, value: Optional[AtomicSwComponentType]) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context_data_prototypes(self, items: list[ApplicationCompositeElementDataPrototype]) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Set context_data_prototypes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_data_prototypes = list(items) if items else []
        return self

    def with_port_prototype(self, value: Optional[PortPrototype]) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Set port_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'port_prototype' is required and cannot be None")
        self._obj.port_prototype = value
        return self

    def with_root_parameter_data_prototype(self, value: Optional[DataPrototype]) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Set root_parameter_data_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'root_parameter_data_prototype' is required and cannot be None")
        self._obj.root_parameter_data_prototype = value
        return self

    def with_target_data_prototype(self, value: Optional[DataPrototype]) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Set target_data_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_data_prototype' is required and cannot be None")
        self._obj.target_data_prototype = value
        return self


    def add_context_data_prototype(self, item: ApplicationCompositeElementDataPrototype) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Add a single item to context_data_prototypes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_data_prototypes.append(item)
        return self

    def clear_context_data_prototypes(self) -> "ParameterInAtomicSWCTypeInstanceRefBuilder":
        """Clear all items from context_data_prototypes list.

        Returns:
            self for method chaining
        """
        self._obj.context_data_prototypes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "contextDataPrototype",
        "portPrototype",
        "rootParameterDataPrototype",
        "targetDataPrototype",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ParameterInAtomicSWCTypeInstanceRef:
        """Build and return the ParameterInAtomicSWCTypeInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj