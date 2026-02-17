"""MsrQueryP1 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class MsrQueryP1(Paginateable):
    """AUTOSAR MsrQueryP1."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "msr_query_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=MsrQueryProps,
        ),  # msrQueryProps
        "msr_query_result": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TopicContent,
        ),  # msrQueryResult
    }

    def __init__(self) -> None:
        """Initialize MsrQueryP1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[TopicContent] = None


class MsrQueryP1Builder:
    """Builder for MsrQueryP1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryP1 = MsrQueryP1()

    def build(self) -> MsrQueryP1:
        """Build and return MsrQueryP1 object.

        Returns:
            MsrQueryP1 instance
        """
        # TODO: Add validation
        return self._obj
