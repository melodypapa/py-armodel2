"""StructuredReq AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 168)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    StandardNameEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class StructuredReq(Paginateable):
    """AUTOSAR StructuredReq."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applies_tos: list[StandardNameEnum]
    conflicts: Optional[DocumentationBlock]
    date: DateTime
    dependencies: Optional[DocumentationBlock]
    description: Optional[DocumentationBlock]
    importance: String
    issued_by: String
    rationale: Optional[DocumentationBlock]
    remark: Optional[DocumentationBlock]
    supporting: Optional[DocumentationBlock]
    tested_items: list[Traceable]
    type: String
    use_case: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize StructuredReq."""
        super().__init__()
        self.applies_tos: list[StandardNameEnum] = []
        self.conflicts: Optional[DocumentationBlock] = None
        self.date: DateTime = None
        self.dependencies: Optional[DocumentationBlock] = None
        self.description: Optional[DocumentationBlock] = None
        self.importance: String = None
        self.issued_by: String = None
        self.rationale: Optional[DocumentationBlock] = None
        self.remark: Optional[DocumentationBlock] = None
        self.supporting: Optional[DocumentationBlock] = None
        self.tested_items: list[Traceable] = []
        self.type: String = None
        self.use_case: Optional[DocumentationBlock] = None
    def serialize(self) -> ET.Element:
        """Serialize StructuredReq to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StructuredReq, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applies_tos (list to container "APPLIES-TOS")
        if self.applies_tos:
            wrapper = ET.Element("APPLIES-TOS")
            for item in self.applies_tos:
                serialized = ARObject._serialize_item(item, "StandardNameEnum")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize conflicts
        if self.conflicts is not None:
            serialized = ARObject._serialize_item(self.conflicts, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFLICTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize date
        if self.date is not None:
            serialized = ARObject._serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dependencies
        if self.dependencies is not None:
            serialized = ARObject._serialize_item(self.dependencies, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEPENDENCIES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize description
        if self.description is not None:
            serialized = ARObject._serialize_item(self.description, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESCRIPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize importance
        if self.importance is not None:
            serialized = ARObject._serialize_item(self.importance, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPORTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize issued_by
        if self.issued_by is not None:
            serialized = ARObject._serialize_item(self.issued_by, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ISSUED-BY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rationale
        if self.rationale is not None:
            serialized = ARObject._serialize_item(self.rationale, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATIONALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remark
        if self.remark is not None:
            serialized = ARObject._serialize_item(self.remark, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMARK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supporting
        if self.supporting is not None:
            serialized = ARObject._serialize_item(self.supporting, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tested_items (list to container "TESTED-ITEMS")
        if self.tested_items:
            wrapper = ET.Element("TESTED-ITEMS")
            for item in self.tested_items:
                serialized = ARObject._serialize_item(item, "Traceable")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize type
        if self.type is not None:
            serialized = ARObject._serialize_item(self.type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_case
        if self.use_case is not None:
            serialized = ARObject._serialize_item(self.use_case, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-CASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StructuredReq":
        """Deserialize XML element to StructuredReq object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StructuredReq object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StructuredReq, cls).deserialize(element)

        # Parse applies_tos (list from container "APPLIES-TOS")
        obj.applies_tos = []
        container = ARObject._find_child_element(element, "APPLIES-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applies_tos.append(child_value)

        # Parse conflicts
        child = ARObject._find_child_element(element, "CONFLICTS")
        if child is not None:
            conflicts_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.conflicts = conflicts_value

        # Parse date
        child = ARObject._find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse dependencies
        child = ARObject._find_child_element(element, "DEPENDENCIES")
        if child is not None:
            dependencies_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.dependencies = dependencies_value

        # Parse description
        child = ARObject._find_child_element(element, "DESCRIPTION")
        if child is not None:
            description_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.description = description_value

        # Parse importance
        child = ARObject._find_child_element(element, "IMPORTANCE")
        if child is not None:
            importance_value = child.text
            obj.importance = importance_value

        # Parse issued_by
        child = ARObject._find_child_element(element, "ISSUED-BY")
        if child is not None:
            issued_by_value = child.text
            obj.issued_by = issued_by_value

        # Parse rationale
        child = ARObject._find_child_element(element, "RATIONALE")
        if child is not None:
            rationale_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.rationale = rationale_value

        # Parse remark
        child = ARObject._find_child_element(element, "REMARK")
        if child is not None:
            remark_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.remark = remark_value

        # Parse supporting
        child = ARObject._find_child_element(element, "SUPPORTING")
        if child is not None:
            supporting_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.supporting = supporting_value

        # Parse tested_items (list from container "TESTED-ITEMS")
        obj.tested_items = []
        container = ARObject._find_child_element(element, "TESTED-ITEMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tested_items.append(child_value)

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = child.text
            obj.type = type_value

        # Parse use_case
        child = ARObject._find_child_element(element, "USE-CASE")
        if child is not None:
            use_case_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.use_case = use_case_value

        return obj



class StructuredReqBuilder:
    """Builder for StructuredReq."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StructuredReq = StructuredReq()

    def build(self) -> StructuredReq:
        """Build and return StructuredReq object.

        Returns:
            StructuredReq instance
        """
        # TODO: Add validation
        return self._obj
