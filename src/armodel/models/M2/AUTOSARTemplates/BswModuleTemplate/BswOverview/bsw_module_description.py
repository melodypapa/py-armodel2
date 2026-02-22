"""BswModuleDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 26)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 973)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 426)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 168)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswOverview.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation.sw_component_documentation import (
    SwComponentDocumentation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_dependency import (
        BswModuleDependency,
    )



class BswModuleDescription(ARElement):
    """AUTOSAR BswModuleDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_refs: list[ARRef]
    bsw_module_documentation: Optional[SwComponentDocumentation]
    expected_entrie_refs: list[ARRef]
    implemented_refs: list[ARRef]
    internal_behaviors: list[BswInternalBehavior]
    module_id: Optional[PositiveInteger]
    provided_clients: list[BswModuleClientServerEntry]
    provided_data_refs: list[ARRef]
    provided_mode_refs: list[ARRef]
    released_trigger_refs: list[ARRef]
    required_clients: list[BswModuleClientServerEntry]
    required_data_refs: list[ARRef]
    required_mode_refs: list[ARRef]
    required_trigger_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswModuleDescription."""
        super().__init__()
        self.bsw_module_refs: list[ARRef] = []
        self.bsw_module_documentation: Optional[SwComponentDocumentation] = None
        self.expected_entrie_refs: list[ARRef] = []
        self.implemented_refs: list[ARRef] = []
        self.internal_behaviors: list[BswInternalBehavior] = []
        self.module_id: Optional[PositiveInteger] = None
        self.provided_clients: list[BswModuleClientServerEntry] = []
        self.provided_data_refs: list[ARRef] = []
        self.provided_mode_refs: list[ARRef] = []
        self.released_trigger_refs: list[ARRef] = []
        self.required_clients: list[BswModuleClientServerEntry] = []
        self.required_data_refs: list[ARRef] = []
        self.required_mode_refs: list[ARRef] = []
        self.required_trigger_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswModuleDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleDescription, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_refs (list to container "BSW-MODULE-REFS")
        if self.bsw_module_refs:
            wrapper = ET.Element("BSW-MODULE-REFS")
            for item in self.bsw_module_refs:
                serialized = SerializationHelper.serialize_item(item, "BswModuleDependency")
                if serialized is not None:
                    child_elem = ET.Element("BSW-MODULE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bsw_module_documentation
        if self.bsw_module_documentation is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_module_documentation, "SwComponentDocumentation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-DOCUMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize expected_entrie_refs (list to container "EXPECTED-ENTRIE-REFS")
        if self.expected_entrie_refs:
            wrapper = ET.Element("EXPECTED-ENTRIE-REFS")
            for item in self.expected_entrie_refs:
                serialized = SerializationHelper.serialize_item(item, "BswModuleEntry")
                if serialized is not None:
                    child_elem = ET.Element("EXPECTED-ENTRIE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implemented_refs (list to container "IMPLEMENTED-REFS")
        if self.implemented_refs:
            wrapper = ET.Element("IMPLEMENTED-REFS")
            for item in self.implemented_refs:
                serialized = SerializationHelper.serialize_item(item, "BswModuleEntry")
                if serialized is not None:
                    child_elem = ET.Element("IMPLEMENTED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_behaviors (list to container "INTERNAL-BEHAVIORS")
        if self.internal_behaviors:
            wrapper = ET.Element("INTERNAL-BEHAVIORS")
            for item in self.internal_behaviors:
                serialized = SerializationHelper.serialize_item(item, "BswInternalBehavior")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize module_id
        if self.module_id is not None:
            serialized = SerializationHelper.serialize_item(self.module_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODULE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_clients (list to container "PROVIDED-CLIENTS")
        if self.provided_clients:
            wrapper = ET.Element("PROVIDED-CLIENTS")
            for item in self.provided_clients:
                serialized = SerializationHelper.serialize_item(item, "BswModuleClientServerEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_data_refs (list to container "PROVIDED-DATA-REFS")
        if self.provided_data_refs:
            wrapper = ET.Element("PROVIDED-DATA-REFS")
            for item in self.provided_data_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("PROVIDED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_mode_refs (list to container "PROVIDED-MODE-REFS")
        if self.provided_mode_refs:
            wrapper = ET.Element("PROVIDED-MODE-REFS")
            for item in self.provided_mode_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("PROVIDED-MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize released_trigger_refs (list to container "RELEASED-TRIGGER-REFS")
        if self.released_trigger_refs:
            wrapper = ET.Element("RELEASED-TRIGGER-REFS")
            for item in self.released_trigger_refs:
                serialized = SerializationHelper.serialize_item(item, "Trigger")
                if serialized is not None:
                    child_elem = ET.Element("RELEASED-TRIGGER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_clients (list to container "REQUIRED-CLIENTS")
        if self.required_clients:
            wrapper = ET.Element("REQUIRED-CLIENTS")
            for item in self.required_clients:
                serialized = SerializationHelper.serialize_item(item, "BswModuleClientServerEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_data_refs (list to container "REQUIRED-DATA-REFS")
        if self.required_data_refs:
            wrapper = ET.Element("REQUIRED-DATA-REFS")
            for item in self.required_data_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_mode_refs (list to container "REQUIRED-MODE-REFS")
        if self.required_mode_refs:
            wrapper = ET.Element("REQUIRED-MODE-REFS")
            for item in self.required_mode_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_trigger_refs (list to container "REQUIRED-TRIGGER-REFS")
        if self.required_trigger_refs:
            wrapper = ET.Element("REQUIRED-TRIGGER-REFS")
            for item in self.required_trigger_refs:
                serialized = SerializationHelper.serialize_item(item, "Trigger")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-TRIGGER-REF")
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
    def deserialize(cls, element: ET.Element) -> "BswModuleDescription":
        """Deserialize XML element to BswModuleDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleDescription, cls).deserialize(element)

        # Parse bsw_module_refs (list from container "BSW-MODULE-REFS")
        obj.bsw_module_refs = []
        container = SerializationHelper.find_child_element(element, "BSW-MODULE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_module_refs.append(child_value)

        # Parse bsw_module_documentation
        child = SerializationHelper.find_child_element(element, "BSW-MODULE-DOCUMENTATION")
        if child is not None:
            bsw_module_documentation_value = SerializationHelper.deserialize_by_tag(child, "SwComponentDocumentation")
            obj.bsw_module_documentation = bsw_module_documentation_value

        # Parse expected_entrie_refs (list from container "EXPECTED-ENTRIE-REFS")
        obj.expected_entrie_refs = []
        container = SerializationHelper.find_child_element(element, "EXPECTED-ENTRIE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.expected_entrie_refs.append(child_value)

        # Parse implemented_refs (list from container "IMPLEMENTED-REFS")
        obj.implemented_refs = []
        container = SerializationHelper.find_child_element(element, "IMPLEMENTED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implemented_refs.append(child_value)

        # Parse internal_behaviors (list from container "INTERNAL-BEHAVIORS")
        obj.internal_behaviors = []
        container = SerializationHelper.find_child_element(element, "INTERNAL-BEHAVIORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_behaviors.append(child_value)

        # Parse module_id
        child = SerializationHelper.find_child_element(element, "MODULE-ID")
        if child is not None:
            module_id_value = child.text
            obj.module_id = module_id_value

        # Parse provided_clients (list from container "PROVIDED-CLIENTS")
        obj.provided_clients = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-CLIENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_clients.append(child_value)

        # Parse provided_data_refs (list from container "PROVIDED-DATA-REFS")
        obj.provided_data_refs = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_data_refs.append(child_value)

        # Parse provided_mode_refs (list from container "PROVIDED-MODE-REFS")
        obj.provided_mode_refs = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-MODE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_mode_refs.append(child_value)

        # Parse released_trigger_refs (list from container "RELEASED-TRIGGER-REFS")
        obj.released_trigger_refs = []
        container = SerializationHelper.find_child_element(element, "RELEASED-TRIGGER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.released_trigger_refs.append(child_value)

        # Parse required_clients (list from container "REQUIRED-CLIENTS")
        obj.required_clients = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-CLIENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_clients.append(child_value)

        # Parse required_data_refs (list from container "REQUIRED-DATA-REFS")
        obj.required_data_refs = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_data_refs.append(child_value)

        # Parse required_mode_refs (list from container "REQUIRED-MODE-REFS")
        obj.required_mode_refs = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-MODE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_mode_refs.append(child_value)

        # Parse required_trigger_refs (list from container "REQUIRED-TRIGGER-REFS")
        obj.required_trigger_refs = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-TRIGGER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_trigger_refs.append(child_value)

        return obj



class BswModuleDescriptionBuilder:
    """Builder for BswModuleDescription with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BswModuleDescription = BswModuleDescription()


    def with_short_name(self, value: Identifier) -> "BswModuleDescriptionBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "BswModuleDescriptionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "BswModuleDescriptionBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "BswModuleDescriptionBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "BswModuleDescriptionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "BswModuleDescriptionBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "BswModuleDescriptionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "BswModuleDescriptionBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "BswModuleDescriptionBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_bsw_modules(self, items: list[BswModuleDependency]) -> "BswModuleDescriptionBuilder":
        """Set bsw_modules list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bsw_modules = list(items) if items else []
        return self

    def with_bsw_module_documentation(self, value: Optional[SwComponentDocumentation]) -> "BswModuleDescriptionBuilder":
        """Set bsw_module_documentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_module_documentation = value
        return self

    def with_expected_entries(self, items: list[BswModuleEntry]) -> "BswModuleDescriptionBuilder":
        """Set expected_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.expected_entries = list(items) if items else []
        return self

    def with_implementeds(self, items: list[BswModuleEntry]) -> "BswModuleDescriptionBuilder":
        """Set implementeds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implementeds = list(items) if items else []
        return self

    def with_internal_behaviors(self, items: list[BswInternalBehavior]) -> "BswModuleDescriptionBuilder":
        """Set internal_behaviors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internal_behaviors = list(items) if items else []
        return self

    def with_module_id(self, value: Optional[PositiveInteger]) -> "BswModuleDescriptionBuilder":
        """Set module_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.module_id = value
        return self

    def with_provided_clients(self, items: list[BswModuleClientServerEntry]) -> "BswModuleDescriptionBuilder":
        """Set provided_clients list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_clients = list(items) if items else []
        return self

    def with_provided_datas(self, items: list[VariableDataPrototype]) -> "BswModuleDescriptionBuilder":
        """Set provided_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_datas = list(items) if items else []
        return self

    def with_provided_modes(self, items: list[ModeDeclarationGroup]) -> "BswModuleDescriptionBuilder":
        """Set provided_modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_modes = list(items) if items else []
        return self

    def with_released_triggers(self, items: list[Trigger]) -> "BswModuleDescriptionBuilder":
        """Set released_triggers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.released_triggers = list(items) if items else []
        return self

    def with_required_clients(self, items: list[BswModuleClientServerEntry]) -> "BswModuleDescriptionBuilder":
        """Set required_clients list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_clients = list(items) if items else []
        return self

    def with_required_datas(self, items: list[VariableDataPrototype]) -> "BswModuleDescriptionBuilder":
        """Set required_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_datas = list(items) if items else []
        return self

    def with_required_modes(self, items: list[ModeDeclarationGroup]) -> "BswModuleDescriptionBuilder":
        """Set required_modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_modes = list(items) if items else []
        return self

    def with_required_triggers(self, items: list[Trigger]) -> "BswModuleDescriptionBuilder":
        """Set required_triggers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_triggers = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "BswModuleDescriptionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "BswModuleDescriptionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_bsw_module(self, item: BswModuleDependency) -> "BswModuleDescriptionBuilder":
        """Add a single item to bsw_modules list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bsw_modules.append(item)
        return self

    def clear_bsw_modules(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from bsw_modules list.

        Returns:
            self for method chaining
        """
        self._obj.bsw_modules = []
        return self

    def add_expected_entrie(self, item: BswModuleEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to expected_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.expected_entries.append(item)
        return self

    def clear_expected_entries(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from expected_entries list.

        Returns:
            self for method chaining
        """
        self._obj.expected_entries = []
        return self

    def add_implemented(self, item: BswModuleEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to implementeds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implementeds.append(item)
        return self

    def clear_implementeds(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from implementeds list.

        Returns:
            self for method chaining
        """
        self._obj.implementeds = []
        return self

    def add_internal_behavior(self, item: BswInternalBehavior) -> "BswModuleDescriptionBuilder":
        """Add a single item to internal_behaviors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internal_behaviors.append(item)
        return self

    def clear_internal_behaviors(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from internal_behaviors list.

        Returns:
            self for method chaining
        """
        self._obj.internal_behaviors = []
        return self

    def add_provided_client(self, item: BswModuleClientServerEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to provided_clients list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_clients.append(item)
        return self

    def clear_provided_clients(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from provided_clients list.

        Returns:
            self for method chaining
        """
        self._obj.provided_clients = []
        return self

    def add_provided_data(self, item: VariableDataPrototype) -> "BswModuleDescriptionBuilder":
        """Add a single item to provided_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_datas.append(item)
        return self

    def clear_provided_datas(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from provided_datas list.

        Returns:
            self for method chaining
        """
        self._obj.provided_datas = []
        return self

    def add_provided_mode(self, item: ModeDeclarationGroup) -> "BswModuleDescriptionBuilder":
        """Add a single item to provided_modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_modes.append(item)
        return self

    def clear_provided_modes(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from provided_modes list.

        Returns:
            self for method chaining
        """
        self._obj.provided_modes = []
        return self

    def add_released_trigger(self, item: Trigger) -> "BswModuleDescriptionBuilder":
        """Add a single item to released_triggers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.released_triggers.append(item)
        return self

    def clear_released_triggers(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from released_triggers list.

        Returns:
            self for method chaining
        """
        self._obj.released_triggers = []
        return self

    def add_required_client(self, item: BswModuleClientServerEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to required_clients list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_clients.append(item)
        return self

    def clear_required_clients(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from required_clients list.

        Returns:
            self for method chaining
        """
        self._obj.required_clients = []
        return self

    def add_required_data(self, item: VariableDataPrototype) -> "BswModuleDescriptionBuilder":
        """Add a single item to required_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_datas.append(item)
        return self

    def clear_required_datas(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from required_datas list.

        Returns:
            self for method chaining
        """
        self._obj.required_datas = []
        return self

    def add_required_mode(self, item: ModeDeclarationGroup) -> "BswModuleDescriptionBuilder":
        """Add a single item to required_modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_modes.append(item)
        return self

    def clear_required_modes(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from required_modes list.

        Returns:
            self for method chaining
        """
        self._obj.required_modes = []
        return self

    def add_required_trigger(self, item: Trigger) -> "BswModuleDescriptionBuilder":
        """Add a single item to required_triggers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_triggers.append(item)
        return self

    def clear_required_triggers(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from required_triggers list.

        Returns:
            self for method chaining
        """
        self._obj.required_triggers = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> BswModuleDescription:
        """Build and return the BswModuleDescription instance with validation."""
        self._validate_instance()
        pass
        return self._obj