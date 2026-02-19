"""MsrQueryP1 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class MsrQueryP1(Paginateable):
    """AUTOSAR MsrQueryP1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result: Optional[TopicContent]
    def __init__(self) -> None:
        """Initialize MsrQueryP1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[TopicContent] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP1":
        """Deserialize XML element to MsrQueryP1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryP1 object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse msr_query_props
        child = ARObject._find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = ARObject._deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result
        child = ARObject._find_child_element(element, "MSR-QUERY-RESULT")
        if child is not None:
            msr_query_result_value = ARObject._deserialize_by_tag(child, "TopicContent")
            obj.msr_query_result = msr_query_result_value

        return obj



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
