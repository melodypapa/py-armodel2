"""DiagnosticTroubleCodeProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticAging.diagnostic_aging import (
    DiagnosticAging,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticExtendedDataRecord.diagnostic_extended_data_record import (
    DiagnosticExtendedDataRecord,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame.diagnostic_freeze_frame import (
    DiagnosticFreezeFrame,
)


class DiagnosticTroubleCodeProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("aging", None, False, False, DiagnosticAging),  # aging
        ("diagnostic_memory", None, False, False, any (DiagnosticMemory)),  # diagnosticMemory
        ("extended_datas", None, False, True, DiagnosticExtendedDataRecord),  # extendedDatas
        ("freeze_frames", None, False, True, DiagnosticFreezeFrame),  # freezeFrames
        ("immediate_nv", None, True, False, None),  # immediateNv
        ("legislated", None, False, False, DiagnosticDataIdentifier),  # legislated
        ("max_number", None, True, False, None),  # maxNumber
        ("priority", None, True, False, None),  # priority
        ("significance", None, False, False, DiagnosticSignificanceEnum),  # significance
        ("snapshot", None, False, False, DiagnosticDataIdentifier),  # snapshot
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeProps."""
        super().__init__()
        self.aging: Optional[DiagnosticAging] = None
        self.diagnostic_memory: Optional[Any] = None
        self.extended_datas: list[DiagnosticExtendedDataRecord] = []
        self.freeze_frames: list[DiagnosticFreezeFrame] = []
        self.immediate_nv: Optional[Boolean] = None
        self.legislated: Optional[DiagnosticDataIdentifier] = None
        self.max_number: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.significance: Optional[DiagnosticSignificanceEnum] = None
        self.snapshot: Optional[DiagnosticDataIdentifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTroubleCodeProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeProps":
        """Create DiagnosticTroubleCodeProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTroubleCodeProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTroubleCodeProps since parent returns ARObject
        return cast("DiagnosticTroubleCodeProps", obj)


class DiagnosticTroubleCodePropsBuilder:
    """Builder for DiagnosticTroubleCodeProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeProps = DiagnosticTroubleCodeProps()

    def build(self) -> DiagnosticTroubleCodeProps:
        """Build and return DiagnosticTroubleCodeProps object.

        Returns:
            DiagnosticTroubleCodeProps instance
        """
        # TODO: Add validation
        return self._obj
