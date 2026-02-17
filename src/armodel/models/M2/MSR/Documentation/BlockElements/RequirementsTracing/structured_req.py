"""StructuredReq AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 168)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)


class StructuredReq(Paginateable):
    """AUTOSAR StructuredReq."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "applies_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=StandardNameEnum,
        ),  # appliesTos
        "conflicts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # conflicts
        "date": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # date
        "dependencies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # dependencies
        "description": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # description
        "importance": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # importance
        "issued_by": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # issuedBy
        "rationale": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # rationale
        "remark": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # remark
        "supporting": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # supporting
        "tested_items": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Traceable,
        ),  # testedItems
        "type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # type
        "use_case": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # useCase
    }

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
