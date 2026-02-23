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
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
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



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class BswModuleDescription(ARElement):
    """AUTOSAR BswModuleDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_modules_dependency: list[BswModuleDependency]
    bsw_module_documentation: Optional[SwComponentDocumentation]
    _expected_entrie_refs: list[ARRef]
    _implemented_entrie_refs: list[ARRef]
    internal_behaviors: list[BswInternalBehavior]
    module_id: Optional[PositiveInteger]
    _provided_client_server_entries: list[BswModuleClientServerEntry]
    provided_datas: list[VariableDataPrototype]
    provided_mode_groups: list[ModeDeclarationGroup]
    released_triggers: list[Trigger]
    _required_client_server_entries: list[BswModuleClientServerEntry]
    required_datas: list[VariableDataPrototype]
    required_mode_groups: list[ModeDeclarationGroup]
    required_triggers: list[Trigger]
    def __init__(self) -> None:
        """Initialize BswModuleDescription."""
        super().__init__()
        self.bsw_modules_dependency: list[BswModuleDependency] = []
        self.bsw_module_documentation: Optional[SwComponentDocumentation] = None
        self._expected_entrie_refs: list[ARRef] = []
        self._implemented_entrie_refs: list[ARRef] = []
        self.internal_behaviors: list[BswInternalBehavior] = []
        self.module_id: Optional[PositiveInteger] = None
        self._provided_client_server_entries: list[BswModuleClientServerEntry] = []
        self.provided_datas: list[VariableDataPrototype] = []
        self.provided_mode_groups: list[ModeDeclarationGroup] = []
        self.released_triggers: list[Trigger] = []
        self._required_client_server_entries: list[BswModuleClientServerEntry] = []
        self.required_datas: list[VariableDataPrototype] = []
        self.required_mode_groups: list[ModeDeclarationGroup] = []
        self.required_triggers: list[Trigger] = []
    @property
    @xml_element_name("EXPECTED-ENTRYS")
    def expected_entrie_refs(self) -> list[ARRef]:
        """Get expected_entrie_refs with custom XML element name."""
        return self._expected_entrie_refs

    @expected_entrie_refs.setter
    def expected_entrie_refs(self, value: list[ARRef]) -> None:
        """Set expected_entrie_refs with custom XML element name."""
        self._expected_entrie_refs = value

    @property
    @xml_element_name("IMPLEMENTED-ENTRYS")
    def implemented_entrie_refs(self) -> list[ARRef]:
        """Get implemented_entrie_refs with custom XML element name."""
        return self._implemented_entrie_refs

    @implemented_entrie_refs.setter
    def implemented_entrie_refs(self, value: list[ARRef]) -> None:
        """Set implemented_entrie_refs with custom XML element name."""
        self._implemented_entrie_refs = value

    @property
    @xml_element_name("PROVIDED-ENTRYS")
    def provided_client_server_entries(self) -> list[BswModuleClientServerEntry]:
        """Get provided_client_server_entries with custom XML element name."""
        return self._provided_client_server_entries

    @provided_client_server_entries.setter
    def provided_client_server_entries(self, value: list[BswModuleClientServerEntry]) -> None:
        """Set provided_client_server_entries with custom XML element name."""
        self._provided_client_server_entries = value

    @property
    @xml_element_name("REQUIRED-ENTRYS")
    def required_client_server_entries(self) -> list[BswModuleClientServerEntry]:
        """Get required_client_server_entries with custom XML element name."""
        return self._required_client_server_entries

    @required_client_server_entries.setter
    def required_client_server_entries(self, value: list[BswModuleClientServerEntry]) -> None:
        """Set required_client_server_entries with custom XML element name."""
        self._required_client_server_entries = value


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

        # Serialize bsw_modules_dependency (list)
        for item in self.bsw_modules_dependency:
            serialized = SerializationHelper.serialize_item(item, "BswModuleDependency")
            if serialized is not None:
                # For non-container lists, wrap with correct tag
                wrapped = ET.Element("BSW-MODULES-DEPENDENCY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize expected_entrie_refs (list to container "EXPECTED-ENTRYS")
        if self.expected_entrie_refs:
            wrapper = ET.Element("EXPECTED-ENTRYS")
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

        # Serialize implemented_entrie_refs (list to container "IMPLEMENTED-ENTRYS")
        if self.implemented_entrie_refs:
            wrapper = ET.Element("IMPLEMENTED-ENTRYS")
            for item in self.implemented_entrie_refs:
                serialized = SerializationHelper.serialize_item(item, "BswModuleEntry")
                if serialized is not None:
                    child_elem = ET.Element("IMPLEMENTED-ENTRIE-REF")
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

        # Serialize provided_client_server_entries (list to container "PROVIDED-ENTRYS")
        if self.provided_client_server_entries:
            wrapper = ET.Element("PROVIDED-ENTRYS")
            for item in self.provided_client_server_entries:
                serialized = SerializationHelper.serialize_item(item, "BswModuleClientServerEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_datas (list to container "PROVIDED-DATAS")
        if self.provided_datas:
            wrapper = ET.Element("PROVIDED-DATAS")
            for item in self.provided_datas:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_mode_groups (list to container "PROVIDED-MODE-GROUPS")
        if self.provided_mode_groups:
            wrapper = ET.Element("PROVIDED-MODE-GROUPS")
            for item in self.provided_mode_groups:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize released_triggers (list to container "RELEASED-TRIGGERS")
        if self.released_triggers:
            wrapper = ET.Element("RELEASED-TRIGGERS")
            for item in self.released_triggers:
                serialized = SerializationHelper.serialize_item(item, "Trigger")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_client_server_entries (list to container "REQUIRED-ENTRYS")
        if self.required_client_server_entries:
            wrapper = ET.Element("REQUIRED-ENTRYS")
            for item in self.required_client_server_entries:
                serialized = SerializationHelper.serialize_item(item, "BswModuleClientServerEntry")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_datas (list to container "REQUIRED-DATAS")
        if self.required_datas:
            wrapper = ET.Element("REQUIRED-DATAS")
            for item in self.required_datas:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_mode_groups (list to container "REQUIRED-MODE-GROUPS")
        if self.required_mode_groups:
            wrapper = ET.Element("REQUIRED-MODE-GROUPS")
            for item in self.required_mode_groups:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_triggers (list to container "REQUIRED-TRIGGERS")
        if self.required_triggers:
            wrapper = ET.Element("REQUIRED-TRIGGERS")
            for item in self.required_triggers:
                serialized = SerializationHelper.serialize_item(item, "Trigger")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse bsw_modules_dependency (list)
        obj.bsw_modules_dependency = []
        for child in SerializationHelper.find_all_child_elements(element, "BSW-MODULES-DEPENDENCY"):
            bsw_modules_dependency_value = SerializationHelper.deserialize_by_tag(child, "BswModuleDependency")
            obj.bsw_modules_dependency.append(bsw_modules_dependency_value)

        # Parse bsw_module_documentation
        child = SerializationHelper.find_child_element(element, "BSW-MODULE-DOCUMENTATION")
        if child is not None:
            bsw_module_documentation_value = SerializationHelper.deserialize_by_tag(child, "SwComponentDocumentation")
            obj.bsw_module_documentation = bsw_module_documentation_value

        # Parse expected_entrie_refs (list from container "EXPECTED-ENTRYS")
        obj.expected_entrie_refs = []
        container = SerializationHelper.find_child_element(element, "EXPECTED-ENTRYS")
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
                    obj.expected_entrie_refs.append(child_value)

        # Parse implemented_entrie_refs (list from container "IMPLEMENTED-ENTRYS")
        obj.implemented_entrie_refs = []
        container = SerializationHelper.find_child_element(element, "IMPLEMENTED-ENTRYS")
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
                    obj.implemented_entrie_refs.append(child_value)

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

        # Parse provided_client_server_entries (list from container "PROVIDED-ENTRYS")
        obj.provided_client_server_entries = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-ENTRYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_client_server_entries.append(child_value)

        # Parse provided_datas (list from container "PROVIDED-DATAS")
        obj.provided_datas = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_datas.append(child_value)

        # Parse provided_mode_groups (list from container "PROVIDED-MODE-GROUPS")
        obj.provided_mode_groups = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-MODE-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_mode_groups.append(child_value)

        # Parse released_triggers (list from container "RELEASED-TRIGGERS")
        obj.released_triggers = []
        container = SerializationHelper.find_child_element(element, "RELEASED-TRIGGERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.released_triggers.append(child_value)

        # Parse required_client_server_entries (list from container "REQUIRED-ENTRYS")
        obj.required_client_server_entries = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-ENTRYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_client_server_entries.append(child_value)

        # Parse required_datas (list from container "REQUIRED-DATAS")
        obj.required_datas = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_datas.append(child_value)

        # Parse required_mode_groups (list from container "REQUIRED-MODE-GROUPS")
        obj.required_mode_groups = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-MODE-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_mode_groups.append(child_value)

        # Parse required_triggers (list from container "REQUIRED-TRIGGERS")
        obj.required_triggers = []
        container = SerializationHelper.find_child_element(element, "REQUIRED-TRIGGERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_triggers.append(child_value)

        return obj



class BswModuleDescriptionBuilder(ARElementBuilder):
    """Builder for BswModuleDescription with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleDescription = BswModuleDescription()


    def with_bsw_modules_dependency(self, items: list[BswModuleDependency]) -> "BswModuleDescriptionBuilder":
        """Set bsw_modules_dependency list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bsw_modules_dependency = list(items) if items else []
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

    def with_implemented_entries(self, items: list[BswModuleEntry]) -> "BswModuleDescriptionBuilder":
        """Set implemented_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implemented_entries = list(items) if items else []
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

    def with_provided_client_server_entries(self, items: list[BswModuleClientServerEntry]) -> "BswModuleDescriptionBuilder":
        """Set provided_client_server_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_client_server_entries = list(items) if items else []
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

    def with_provided_mode_groups(self, items: list[ModeDeclarationGroup]) -> "BswModuleDescriptionBuilder":
        """Set provided_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_mode_groups = list(items) if items else []
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

    def with_required_client_server_entries(self, items: list[BswModuleClientServerEntry]) -> "BswModuleDescriptionBuilder":
        """Set required_client_server_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_client_server_entries = list(items) if items else []
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

    def with_required_mode_groups(self, items: list[ModeDeclarationGroup]) -> "BswModuleDescriptionBuilder":
        """Set required_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_mode_groups = list(items) if items else []
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


    def add_bsw_modules_dependenc(self, item: BswModuleDependency) -> "BswModuleDescriptionBuilder":
        """Add a single item to bsw_modules_dependency list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bsw_modules_dependency.append(item)
        return self

    def clear_bsw_modules_dependency(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from bsw_modules_dependency list.

        Returns:
            self for method chaining
        """
        self._obj.bsw_modules_dependency = []
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

    def add_implemented_entrie(self, item: BswModuleEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to implemented_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implemented_entries.append(item)
        return self

    def clear_implemented_entries(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from implemented_entries list.

        Returns:
            self for method chaining
        """
        self._obj.implemented_entries = []
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

    def add_provided_client_server_entrie(self, item: BswModuleClientServerEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to provided_client_server_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_client_server_entries.append(item)
        return self

    def clear_provided_client_server_entries(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from provided_client_server_entries list.

        Returns:
            self for method chaining
        """
        self._obj.provided_client_server_entries = []
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

    def add_provided_mode_group(self, item: ModeDeclarationGroup) -> "BswModuleDescriptionBuilder":
        """Add a single item to provided_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_mode_groups.append(item)
        return self

    def clear_provided_mode_groups(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from provided_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.provided_mode_groups = []
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

    def add_required_client_server_entrie(self, item: BswModuleClientServerEntry) -> "BswModuleDescriptionBuilder":
        """Add a single item to required_client_server_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_client_server_entries.append(item)
        return self

    def clear_required_client_server_entries(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from required_client_server_entries list.

        Returns:
            self for method chaining
        """
        self._obj.required_client_server_entries = []
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

    def add_required_mode_group(self, item: ModeDeclarationGroup) -> "BswModuleDescriptionBuilder":
        """Add a single item to required_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_mode_groups.append(item)
        return self

    def clear_required_mode_groups(self) -> "BswModuleDescriptionBuilder":
        """Clear all items from required_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.required_mode_groups = []
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