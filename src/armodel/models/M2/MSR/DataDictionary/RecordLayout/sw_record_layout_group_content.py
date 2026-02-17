"""SwRecordLayoutGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_v import (
    SwRecordLayoutV,
)


class SwRecordLayoutGroupContent(ARObject):
    """AUTOSAR SwRecordLayoutGroupContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_record": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwRecordLayoutGroup,
        ),  # swRecord
        "sw_record_layout_v": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwRecordLayoutV,
        ),  # swRecordLayoutV
    }

    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroupContent."""
        super().__init__()
        self.sw_record: Optional[SwRecordLayoutGroup] = None
        self.sw_record_layout_v: Optional[SwRecordLayoutV] = None


class SwRecordLayoutGroupContentBuilder:
    """Builder for SwRecordLayoutGroupContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutGroupContent = SwRecordLayoutGroupContent()

    def build(self) -> SwRecordLayoutGroupContent:
        """Build and return SwRecordLayoutGroupContent object.

        Returns:
            SwRecordLayoutGroupContent instance
        """
        # TODO: Add validation
        return self._obj
