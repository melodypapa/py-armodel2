"""PortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 304)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 62)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 66)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 236)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 30)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 458)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.delegated_port_annotation import (
    DelegatedPortAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.mode_port_annotation import (
    ModePortAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.trigger_port_annotation import (
    TriggerPortAnnotation,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.client_server_annotation import (
        ClientServerAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.io_hw_abstraction_server_annotation import (
        IoHwAbstractionServerAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.nv_data_port_annotation import (
        NvDataPortAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.parameter_port_annotation import (
        ParameterPortAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
        SenderReceiverAnnotation,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PortPrototype(Identifiable, ABC):
    """AUTOSAR PortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    client_server_annotations: list[ClientServerAnnotation]
    delegated_port_annotation: Optional[DelegatedPortAnnotation]
    io_hw_abstraction_server_annotations: list[IoHwAbstractionServerAnnotation]
    mode_port_annotations: list[ModePortAnnotation]
    nv_data_port_annotations: list[NvDataPortAnnotation]
    parameter_port_annotations: list[ParameterPortAnnotation]
    sender_receiver_annotations: list[SenderReceiverAnnotation]
    trigger_port_annotations: list[TriggerPortAnnotation]
    _DESERIALIZE_DISPATCH = {
        "CLIENT-SERVER-ANNOTATIONS": lambda obj, elem: obj.client_server_annotations.append(SerializationHelper.deserialize_by_tag(elem, "ClientServerAnnotation")),
        "DELEGATED-PORT-ANNOTATION": lambda obj, elem: setattr(obj, "delegated_port_annotation", SerializationHelper.deserialize_by_tag(elem, "DelegatedPortAnnotation")),
        "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS": lambda obj, elem: obj.io_hw_abstraction_server_annotations.append(SerializationHelper.deserialize_by_tag(elem, "IoHwAbstractionServerAnnotation")),
        "MODE-PORT-ANNOTATIONS": lambda obj, elem: obj.mode_port_annotations.append(SerializationHelper.deserialize_by_tag(elem, "ModePortAnnotation")),
        "NV-DATA-PORT-ANNOTATIONS": lambda obj, elem: obj.nv_data_port_annotations.append(SerializationHelper.deserialize_by_tag(elem, "NvDataPortAnnotation")),
        "PARAMETER-PORT-ANNOTATIONS": lambda obj, elem: obj.parameter_port_annotations.append(SerializationHelper.deserialize_by_tag(elem, "ParameterPortAnnotation")),
        "SENDER-RECEIVER-ANNOTATIONS": ("_POLYMORPHIC_LIST", "sender_receiver_annotations", ["ReceiverAnnotation", "SenderAnnotation"]),
        "TRIGGER-PORT-ANNOTATIONS": lambda obj, elem: obj.trigger_port_annotations.append(SerializationHelper.deserialize_by_tag(elem, "TriggerPortAnnotation")),
    }


    def __init__(self) -> None:
        """Initialize PortPrototype."""
        super().__init__()
        self.client_server_annotations: list[ClientServerAnnotation] = []
        self.delegated_port_annotation: Optional[DelegatedPortAnnotation] = None
        self.io_hw_abstraction_server_annotations: list[IoHwAbstractionServerAnnotation] = []
        self.mode_port_annotations: list[ModePortAnnotation] = []
        self.nv_data_port_annotations: list[NvDataPortAnnotation] = []
        self.parameter_port_annotations: list[ParameterPortAnnotation] = []
        self.sender_receiver_annotations: list[SenderReceiverAnnotation] = []
        self.trigger_port_annotations: list[TriggerPortAnnotation] = []

    def serialize(self) -> ET.Element:
        """Serialize PortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_server_annotations (list to container "CLIENT-SERVER-ANNOTATIONS")
        if self.client_server_annotations:
            wrapper = ET.Element("CLIENT-SERVER-ANNOTATIONS")
            for item in self.client_server_annotations:
                serialized = SerializationHelper.serialize_item(item, "ClientServerAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize delegated_port_annotation
        if self.delegated_port_annotation is not None:
            serialized = SerializationHelper.serialize_item(self.delegated_port_annotation, "DelegatedPortAnnotation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DELEGATED-PORT-ANNOTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize io_hw_abstraction_server_annotations (list to container "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
        if self.io_hw_abstraction_server_annotations:
            wrapper = ET.Element("IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
            for item in self.io_hw_abstraction_server_annotations:
                serialized = SerializationHelper.serialize_item(item, "IoHwAbstractionServerAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_port_annotations (list to container "MODE-PORT-ANNOTATIONS")
        if self.mode_port_annotations:
            wrapper = ET.Element("MODE-PORT-ANNOTATIONS")
            for item in self.mode_port_annotations:
                serialized = SerializationHelper.serialize_item(item, "ModePortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_data_port_annotations (list to container "NV-DATA-PORT-ANNOTATIONS")
        if self.nv_data_port_annotations:
            wrapper = ET.Element("NV-DATA-PORT-ANNOTATIONS")
            for item in self.nv_data_port_annotations:
                serialized = SerializationHelper.serialize_item(item, "NvDataPortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_port_annotations (list to container "PARAMETER-PORT-ANNOTATIONS")
        if self.parameter_port_annotations:
            wrapper = ET.Element("PARAMETER-PORT-ANNOTATIONS")
            for item in self.parameter_port_annotations:
                serialized = SerializationHelper.serialize_item(item, "ParameterPortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sender_receiver_annotations (list to container "SENDER-RECEIVER-ANNOTATIONS")
        if self.sender_receiver_annotations:
            wrapper = ET.Element("SENDER-RECEIVER-ANNOTATIONS")
            for item in self.sender_receiver_annotations:
                serialized = SerializationHelper.serialize_item(item, "SenderReceiverAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize trigger_port_annotations (list to container "TRIGGER-PORT-ANNOTATIONS")
        if self.trigger_port_annotations:
            wrapper = ET.Element("TRIGGER-PORT-ANNOTATIONS")
            for item in self.trigger_port_annotations:
                serialized = SerializationHelper.serialize_item(item, "TriggerPortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototype":
        """Deserialize XML element to PortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLIENT-SERVER-ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.client_server_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerAnnotation"))
            elif tag == "DELEGATED-PORT-ANNOTATION":
                setattr(obj, "delegated_port_annotation", SerializationHelper.deserialize_by_tag(child, "DelegatedPortAnnotation"))
            elif tag == "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.io_hw_abstraction_server_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "IoHwAbstractionServerAnnotation"))
            elif tag == "MODE-PORT-ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_port_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "ModePortAnnotation"))
            elif tag == "NV-DATA-PORT-ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nv_data_port_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "NvDataPortAnnotation"))
            elif tag == "PARAMETER-PORT-ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.parameter_port_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterPortAnnotation"))
            elif tag == "SENDER-RECEIVER-ANNOTATIONS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "RECEIVER-ANNOTATION":
                        obj.sender_receiver_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "ReceiverAnnotation"))
                    elif concrete_tag == "SENDER-ANNOTATION":
                        obj.sender_receiver_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "SenderAnnotation"))
            elif tag == "TRIGGER-PORT-ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.trigger_port_annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "TriggerPortAnnotation"))

        return obj



class PortPrototypeBuilder(IdentifiableBuilder):
    """Builder for PortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortPrototype = PortPrototype()


    def with_client_server_annotations(self, items: list[ClientServerAnnotation]) -> "PortPrototypeBuilder":
        """Set client_server_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_server_annotations = list(items) if items else []
        return self

    def with_delegated_port_annotation(self, value: Optional[DelegatedPortAnnotation]) -> "PortPrototypeBuilder":
        """Set delegated_port_annotation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'delegated_port_annotation' is required and cannot be None")
        self._obj.delegated_port_annotation = value
        return self

    def with_io_hw_abstraction_server_annotations(self, items: list[IoHwAbstractionServerAnnotation]) -> "PortPrototypeBuilder":
        """Set io_hw_abstraction_server_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = list(items) if items else []
        return self

    def with_mode_port_annotations(self, items: list[ModePortAnnotation]) -> "PortPrototypeBuilder":
        """Set mode_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = list(items) if items else []
        return self

    def with_nv_data_port_annotations(self, items: list[NvDataPortAnnotation]) -> "PortPrototypeBuilder":
        """Set nv_data_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = list(items) if items else []
        return self

    def with_parameter_port_annotations(self, items: list[ParameterPortAnnotation]) -> "PortPrototypeBuilder":
        """Set parameter_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_port_annotations = list(items) if items else []
        return self

    def with_sender_receiver_annotations(self, items: list[SenderReceiverAnnotation]) -> "PortPrototypeBuilder":
        """Set sender_receiver_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sender_receiver_annotations = list(items) if items else []
        return self

    def with_trigger_port_annotations(self, items: list[TriggerPortAnnotation]) -> "PortPrototypeBuilder":
        """Set trigger_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = list(items) if items else []
        return self


    def add_client_server_annotation(self, item: ClientServerAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to client_server_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_server_annotations.append(item)
        return self

    def clear_client_server_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from client_server_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.client_server_annotations = []
        return self

    def add_io_hw_abstraction_server_annotation(self, item: IoHwAbstractionServerAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to io_hw_abstraction_server_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations.append(item)
        return self

    def clear_io_hw_abstraction_server_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from io_hw_abstraction_server_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = []
        return self

    def add_mode_port_annotation(self, item: ModePortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to mode_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations.append(item)
        return self

    def clear_mode_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from mode_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = []
        return self

    def add_nv_data_port_annotation(self, item: NvDataPortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to nv_data_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations.append(item)
        return self

    def clear_nv_data_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from nv_data_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = []
        return self

    def add_parameter_port_annotation(self, item: ParameterPortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to parameter_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_port_annotations.append(item)
        return self

    def clear_parameter_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from parameter_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_port_annotations = []
        return self

    def add_sender_receiver_annotation(self, item: SenderReceiverAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to sender_receiver_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sender_receiver_annotations.append(item)
        return self

    def clear_sender_receiver_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from sender_receiver_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.sender_receiver_annotations = []
        return self

    def add_trigger_port_annotation(self, item: TriggerPortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to trigger_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations.append(item)
        return self

    def clear_trigger_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from trigger_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "clientServerAnnotation",
        "delegatedPortAnnotation",
        "ioHwAbstractionServerAnnotation",
        "modePortAnnotation",
        "nvDataPortAnnotation",
        "parameterPortAnnotation",
        "senderReceiverAnnotation",
        "triggerPortAnnotation",
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
    def build(self) -> PortPrototype:
        """Build and return the PortPrototype instance (abstract)."""
        raise NotImplementedError