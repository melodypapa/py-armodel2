"""SwRecordLayoutV AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutV(ARObject):
    """AUTOSAR SwRecordLayoutV."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_type: Optional[SwBaseType]
    desc: Optional[MultiLanguageOverviewParagraph]
    short_label: Optional[Identifier]
    sw_generic_axis_param: Optional[SwGenericAxisParam]
    sw_record: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize SwRecordLayoutV."""
        super().__init__()
        self.base_type: Optional[SwBaseType] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
        self.sw_record: Optional[NameToken] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutV":
        """Deserialize XML element to SwRecordLayoutV object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutV object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_type
        child = ARObject._find_child_element(element, "BASE-TYPE")
        if child is not None:
            base_type_value = ARObject._deserialize_by_tag(child, "SwBaseType")
            obj.base_type = base_type_value

        # Parse desc
        child = ARObject._find_child_element(element, "DESC")
        if child is not None:
            desc_value = ARObject._deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        # Parse sw_generic_axis_param
        child = ARObject._find_child_element(element, "SW-GENERIC-AXIS-PARAM")
        if child is not None:
            sw_generic_axis_param_value = ARObject._deserialize_by_tag(child, "SwGenericAxisParam")
            obj.sw_generic_axis_param = sw_generic_axis_param_value

        # Parse sw_record
        child = ARObject._find_child_element(element, "SW-RECORD")
        if child is not None:
            sw_record_value = child.text
            obj.sw_record = sw_record_value

        return obj



class SwRecordLayoutVBuilder:
    """Builder for SwRecordLayoutV."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutV = SwRecordLayoutV()

    def build(self) -> SwRecordLayoutV:
        """Build and return SwRecordLayoutV object.

        Returns:
            SwRecordLayoutV instance
        """
        # TODO: Add validation
        return self._obj
