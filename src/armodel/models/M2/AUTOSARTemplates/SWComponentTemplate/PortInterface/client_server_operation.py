"""ClientServerOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 309)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 102)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2008)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 218)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 433)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)


class ClientServerOperation(Identifiable):
    """AUTOSAR ClientServerOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    argument_refs: list[ARRef]
    diag_arg_integrity: Optional[Boolean]
    possible_errors: list[ApplicationError]
    def __init__(self) -> None:
        """Initialize ClientServerOperation."""
        super().__init__()
        self.argument_refs: list[ARRef] = []
        self.diag_arg_integrity: Optional[Boolean] = None
        self.possible_errors: list[ApplicationError] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerOperation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize argument_refs (list to container "ARGUMENT-REFS")
        if self.argument_refs:
            wrapper = ET.Element("ARGUMENT-REFS")
            for item in self.argument_refs:
                serialized = ARObject._serialize_item(item, "ArgumentDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("ARGUMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize diag_arg_integrity
        if self.diag_arg_integrity is not None:
            serialized = ARObject._serialize_item(self.diag_arg_integrity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-ARG-INTEGRITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize possible_errors (list to container "POSSIBLE-ERRORS")
        if self.possible_errors:
            wrapper = ET.Element("POSSIBLE-ERRORS")
            for item in self.possible_errors:
                serialized = ARObject._serialize_item(item, "ApplicationError")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperation":
        """Deserialize XML element to ClientServerOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperation, cls).deserialize(element)

        # Parse argument_refs (list from container "ARGUMENT-REFS")
        obj.argument_refs = []
        container = ARObject._find_child_element(element, "ARGUMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.argument_refs.append(child_value)

        # Parse diag_arg_integrity
        child = ARObject._find_child_element(element, "DIAG-ARG-INTEGRITY")
        if child is not None:
            diag_arg_integrity_value = child.text
            obj.diag_arg_integrity = diag_arg_integrity_value

        # Parse possible_errors (list from container "POSSIBLE-ERRORS")
        obj.possible_errors = []
        container = ARObject._find_child_element(element, "POSSIBLE-ERRORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.possible_errors.append(child_value)

        return obj



class ClientServerOperationBuilder:
    """Builder for ClientServerOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperation = ClientServerOperation()

    def build(self) -> ClientServerOperation:
        """Build and return ClientServerOperation object.

        Returns:
            ClientServerOperation instance
        """
        # TODO: Add validation
        return self._obj
