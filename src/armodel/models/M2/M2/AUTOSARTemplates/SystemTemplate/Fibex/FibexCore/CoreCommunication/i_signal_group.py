"""ISignalGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)


class ISignalGroup(FibexElement):
    """AUTOSAR ISignalGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "com_based": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # comBased
        "i_signals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignal,
        ),  # iSignals
        "system_signal_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignalGroup,
        ),  # systemSignalGroup
        "transformation_i_signals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (TransformationISignal),
        ),  # transformationISignals
    }

    def __init__(self) -> None:
        """Initialize ISignalGroup."""
        super().__init__()
        self.com_based: Optional[DataTransformation] = None
        self.i_signals: list[ISignal] = []
        self.system_signal_group: Optional[SystemSignalGroup] = None
        self.transformation_i_signals: list[Any] = []


class ISignalGroupBuilder:
    """Builder for ISignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalGroup = ISignalGroup()

    def build(self) -> ISignalGroup:
        """Build and return ISignalGroup object.

        Returns:
            ISignalGroup instance
        """
        # TODO: Add validation
        return self._obj
